# -*- coding:utf-8 -*-
import socket

import threading
import time
from netaddr import IPNetwork, IPAddress

import os
import struct
from ctypes import *

#host que ouvirá
host = "192.168.1.9"

# sub-rede alvo
subnet = "192.168.1.0/24"

#string mágica em relação à qual verificaremos as respostas ICMP
magic_message = "PYTHONRULES!"

def udp_sender(subnet, magic_message):
    time.sleep(5)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for ip in IPNetwork(subnet):
        try:
            #print('send to ',ip)
            sender.sendto(magic_message, ("%s"%(ip, 65212)))
        except:
            pass

t = threading.Thread(target=udp_sender, args=(subnet, magic_message))
t.start()

#nosso cabeçalho IP
class IP(Structure):

    _fields_ = [
            ("ihl", c_ubyte, 4),
            ("version", c_ubyte,4),
            ("tos", c_ubyte),
            ("len",c_ushort),
            ("id", c_ushort),
            ("offset", c_ushort),
            ("ttl", c_ubyte),
            ("protocol_num", c_ubyte),
            ("sum", c_ushort),
            ("src",c_uint32),
            ("dst", c_uint32)
            ]
    
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        #mapeia constantes do protocolo aos seus nomes
        self.protocol_map = {1:"ICMP", 6:"TCP",17:"UDP"}

        #endereços de IP legíveis aos seres humanos
        self.src_address = socket.inet_ntoa(struct.pack("@I",self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

        # protocolo legível aos seres humanos
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

class ICMP(Structure):

    _fields_ = [
            ("type", c_byte),
            ("code", c_ubyte),
            ("checksum", c_ushort),
            ("unused",c_ushort),
            ("next_hop_mtu",c_ushort),
            ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass

if os.name == 'nt':
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP


sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host,0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


try:
    while True:
        #lê um pacote
        raw_buffer = sniffer.recvfrom(65565)[0]

        #cria um cabeçalho IP a partir dos 20 primeiros bytes do buffer
        #ip_header = IP(raw_buffer[0:20])
        ip_header =  IP(raw_buffer)

        #exibe o protocolo detectado e os hosts
        print('Protocol: %s %s -> %s'%(ip_header.protocol, ip_header.src_address, ip_header.dst_address))

        # se for ICMP, nós queremos o pacote
        if ip_header.protocol == "ICMP":

            #calcula em que ponto nosso pacote ICMP começa
            offset = ip_header.ihl * 4
            buf = raw_buffer[offset:offset + sizeof(ICMP)]

            #cria nossa estrutura ICMP
            icmp_header = ICMP(buf)

            print('ICMP -> Type: %d Code: %d'%(icmp_header.type, icmp_header.code))

            #verifica se TYPE e CODE são iguais a 3
            if icmp_header.code == 3 and icmp_header.type == 3:

                #garante que o host está em nossa sub-rede alvo
                if IPAddress(ip_header.src_address) in IPNetwork(subnet):

                    #garante que contém a nossa mensagem mágica
                    if raw_buffer[len(raw_buffer)- len(magic_message):] == magic_message:
                        print('Host Up: %s'%(ip_header.src_address))

# trata o CTRL + C
except KeyboardInterrupt:

    # se estivermos usando o Windows, desabilita o modo promiscuo
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

