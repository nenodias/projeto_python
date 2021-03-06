# -*- coding: utf-8 -*-
import threading
import paramiko
import subprocess
import sys

ip = sys.argv[1]
user = sys.argv[2]
passwd = sys.argv[3]

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    #client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return None

ssh_command(ip, user, passwd, 'id')
