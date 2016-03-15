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
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print("BHP Net Tool")
    print("")
    print("Usage python-netcat.py -t target_host -p port")
    print("-l listen                - listen on [host]:[port] por incoming conn\
    ections")
    print("-e --execute=file_to_run - execute given file upon receiving a conne\
    ction")
    print("-c --command             - initialize a command shell ")
    print("-u --upload=destination  - upon receiving connection upload a file a\
    nd write to [destination]")
    print("")
    print("")
    print("Examples: ")
    print("python-netcat.py -t 192.168.0.1 -p 5555 -l -c")
    print("python-netcat.py -t 192.168.0.1 -p 5555 -l -u=C\\target.exe ")
    print("echo 'ABCDEFGHI' | ./python-netcat.py -t 192.168.11.12 -p 135")
    print("python-netcat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\" ")
    sys.exit(0)

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
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err) )
        usage()

if __name__ == '__main__':
    main()
