# -*- coding:utf-8 -*-
import re
import zlib
import cv2

from scapy.all import *

pictures_directory = '/home/nenodias/pic_carver/pictures'
faces_directory = '/home/nenodias/pic_carver/faces'
pcap_file = 'bhp.pcap'

def get_http_headers(http_payload):
    try:
        #separa os cabeçalhos se for tráfego http
        headers_raw = http_payload[:http_payload.index('\r\n\r\n')+2]

        #divido os campos dos cabeçalhos
        headers = dict(re.findall(r'(?P<name>.*?): (?P<value>.*?)\r\n', headers_raw))
    except:
        return None

    if 'Content-Type' not in headers:
        return None
    return headers

def extract_image(headers, http_payload):
    image = None
    image_type = None

def http_assembler(pcap_file):
    carved_images = 0
    faces_detected = 0

    a = rdpcap(pcap_file)

    sessions = a.sessions()

    for session in sessions:
        http_payload = ''

        for packet in sessions[session]:

            try:
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                    # recompõe o stream
                    http_payload += str(packet[TCP].payload)
            except:
                pass

            headers = get_http_headers(http_payload)

            if headers is None:
                continue


            image, image_type = extract_image(headers, http_payload)

            if image is not None and image_type is not None:

                # armazena a imagem
                file_name = '%s-pic_carver_%d.%s'%(pcap_file, carved_images, image_type)

                arquivo = '%s/%s'%(pictures_directory,file_name)

                fd = open(arquivo,'wb')
                fd.write(image)
                fd.close()

                carved_images += 1


                #agora tenta efetuar uma detecção facial
                try:
                    result = faces_detect(arquivo)
                    if result is True:
                        faces_detected += 1
                except:
                    pass
    return carved_images, faces_detect


carved_images, faces_detected = http_assembler(pcap_file)

print('Extracted: %d images'%(carved_images))
print('Detected: %d images'%(faces_detected))
