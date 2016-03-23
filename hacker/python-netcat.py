# *-* coding:utf-8 *-*
import os
import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0

def usage():
    print('BHP Net Tool')
    print('')
    print('Usage python-netcat.py -t target_host -p port')
    print('-l listen                - listen on [host]:[port] por incoming conn\
    ections')
    print('-e --execute=file_to_run - execute given file upon receiving a conne\
    ction')
    print('-c --command             - initialize a command shell ')
    print('-u --upload=destination  - upon receiving connection upload a file a\
    nd write to [destination]')
    print('')
    print('')
    print('Examples: ')
    print('python-netcat.py -t 192.168.0.1 -p 5555 -l -c')
    print('python-netcat.py -t 192.168.0.1 -p 5555 -l -u=C\\target.exe ')
    print('echo \'ABCDEFGHI\' | ./python-netcat.py -t 192.168.11.12 -p 135')
    print('python-netcat.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd" ')
    sys.exit(0)

def client_sender(buff):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # conecta-se ao nosso host-alvo
        client.connect((target, port))
        if len(buff):
            client.send(buff)
        while True:
            # agora espera receber dados de volta
            recv_len = 1
            response = ''

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            print(response)

            # espera mais dados de entrada
            buff = input('')
            buff += '\n'

            # envia os dados
            client.send(buff)
    except:
        print('[*] Exception! Exiting.')

        # encerra a conexão
        client.close()

def server_loop():
    global target
    global port

    # se não houver nenhum alvo definido, ouviremos todas as interfaces
    if not len(target):
        target = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # dispara uma thread para cuidar de nosso novo cliente
        client_thread = threading.Thread(target=client_handler, args=[client_socket])
        client_thread.start()

def run_command(command):

    # remove a quebra de linha
    command = command.rstrip()

    # executa o comando e obtém os dados de saída
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = 'Failed to execute command.\r\n'

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if  not len(sys.argv[1:]):
        usage()
    # lê as opções de linha de comando
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hle:t:p:cu:', ['help', 'listen', 'execute', 'target', 'port', 'command', 'upload'])
    except getopt.GetoptError as err:
        print(str(err) )
        usage()

    for o, a in opts:
        if o in('-h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = True
        elif o in ('-c', '--commandshell'):
            command = True
        elif o in ('-u', '--upload'):
            upload_destination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False, 'Unhandled Option'

    # iremos ouvir ou simplesmente enviar dados de stdin?
    if not listen and len(target) and port > 0:
        # Lê o buffer da linha de comando
        # isso causará um bloqueio, portanto envie um CTRL+D se não estiver 
        # enviando dados de entrada para stdin
        buff = sys.stdin.read()

        # send data off
        client_sender(buff)
    # Iremos ouvir a porta e potencialmente
    # faremos upload de dados, executaremos comandos e deixaremos um shell
    # de acordo com as opções de linha de comando anteriores
    if listen:
        server_loop()

        


if __name__ == '__main__':
    main()
