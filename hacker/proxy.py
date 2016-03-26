# *-* coding:utf-8 *-*
import os
import sys
import socket
import threading

def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2

    for i in range(0, len(src), length):
        s = src[ i : i + length ]
        hexa = b' '.join( ['%0*X' %(digits, ord(x)) for x in s ] )
        text = b''.join([ x if 0x20 <= ord(x) < 0x7F else b'.' for x in s ])
        result.append( b'%04X  %-*s  %s' %(i , length * ( digits + 1 ) ), hexa, text )
    print(b'\n'.join(result))

def receive_from(connection):
    data_buffer = ''

    # definimos um timeout de 2 segundos; de acordo com
    # seu alvo, pode ser que esse valor precise ser ajustado
    connection.set_timeout(2)

    try:
        # continua lendo em buffer até
        # que não haja mais dados
        # ou a temporização expire
        while True:
            data = connection.recv(4096)

            if not data:
                break

            data_buffer += data
    except:
        pass
    return data_buffer

# modifica qualquer solicitação destinada ao host remoto
def request_handler(data_buffer):
    # faz modificações no pacote
    return data_buffer

# modifica qualquer resposta destinada ao host local
def response_handler(data_buffer):
    # faz modificações no pacote
    return data_buffer

def proxy_handler(client_socket, remotehost, remoteport, receive_first):
    # conecta-se ao host remoto
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remotehost, remoteport))

    # recebe dados
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        # envia os dados ao nosso handler de resposta
        remote_buffer = response_handler(remote_buffer)

        # se houver dados para serem enviados ao nosso cliente local, envia-os
        if len(remote_buffer):
            print('[<==] Sending %d bytes to localhost' %( len(remote_buffer) ) )
            client_socket.send(remote_buffer)
    # agora vamos entrar no laço e ler do host local
    # enviar para o host remoto, enviar para o host local,
    # enxaguar, lavar e repetir
    while True:
        # lê do host local
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            print('[==>] Received %d bytes from localhost' %( len(local_buffer) ) )
            hexdump(local_buffer)

            # envia os dados para o nosso handler de solicitações
            local_buffer = request_handler(local_buffer)

            # envia os dados ao host remoto
            remote_socket.send(local_buffer)
            print('[==>] Sent to remote')
        # recebe a resposta 
        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print('[<==] Received %d bytes from remote' %(remote_buffer) )
            hexdump(remote_buffer)

            # envia dados ao nosso handler de resposta
            remote_buffer = response_handler(remote_buffer)

            # envia a resposta para o socket local
            client_socket.send(remote_buffer)

            print('[<==] Sent to localhost')

        # se não houver mais dados em nenhum dos lados, encerra as conexões
        if not len(local_buffer) or not len(remote_buffer) :
            client_socket.close()
            remote_socket.close()
            print('[*] No more data, Closing connections')

            break

def server_loop(localhost, localport, remotehost, remoteport, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind( (localhost, localport) )
    except:
        print('[!!] Failed to listen on %s:%d' %(localhost, localport) )
        print('[!!] Check for other listening sockets or correct permissions.')
        sys.exit(0)

    print('[*] Listening on %s:%d' %(localhost, localport) )
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # exibe informações sobre a conexão local
        print('[==>] Received incoming connection from %s:%d' %(addr[0], addr[1]))

        # inicia uma thread para conversar com o host remoto
        proxy_thread = threading.Thread(target=proxy_handler, args=[client_socket, remotehost, remoteport, receive_first])

        proxy_thread.start()
def main():
    # sem parsing sofisticado de linha de comando nesse caso
    if len(sys.argv[1:]) != 5:
        print('Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]')
        print('Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True')
        sys.exit(0)

    # define parâmetros para ouvir localmente
    localhost = sys.argv[1]
    localport = sys.argv[2]

    remotehost = sys.argv[3]
    remoteport = sys.argv[4]

    # o código a seguir diz ao nosso proxy para conectar e receber dados
    # antes de enviar ao host remoto
    receive_first = sys.argv[5]

    if 'True' in receive_first:
        receive_first = True
    else:
        receive_first = False

    # agora coloca em ação o nosso socket que ficará ouvindo
    server_loop(localhost, localport, remotehost, remoteport, receive_first)

if __name__ == '__main__':
    main()