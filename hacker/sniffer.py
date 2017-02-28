# -*- coding:utf-8 -*-
import socket
import os

#host que ouvirá
host = "192.168.1.9"

#cria um socket puro e associa-o à interface pública
if os.name == 'nt':
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP


sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# queremos os cabeçalhos IP incluídos na captura
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# se estivermos usando windows, devemos enviar um IOCTL
# para configurar o modo promiscuo
if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# lê um único pacote
print( sniffer.recvfrom(65565) )

#se estivermos usando o windows, desabilitará o modo promíscuo
if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
