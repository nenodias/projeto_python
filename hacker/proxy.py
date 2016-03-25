# *-* coding:utf-8 *-*
import os
import sys
import socket
import threading

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