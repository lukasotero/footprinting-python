#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from scapy.all import *


def main():
    ipDst = input('IP a escanear: ') 
    
    p_icmp = IP(dst=ipDst)/ICMP()
    response = sr1(p_icmp)
    ttl = response.ttl

    # Valor TTL
    print(f"El valor TTL de la respuesta es: {ttl}")

    if (ttl <= 64):
        print("Sistema operativo: Linux")
    elif (ttl <= 128):
        print("Sistema operativo: Windows")
    elif (ttl <= 255):
        print("Sistema operativo: Mac OS")
    else:
        print("Sistema operativo: Desconocido")


if __name__ == '__main__':
    main()
