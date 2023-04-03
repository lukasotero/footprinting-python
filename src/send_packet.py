#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *


def main():
    p_icmp = IP(dst='192.168.10.130')/ICMP()
    response = sr1(p_icmp)
    ttl = response.ttl

    if (ttl == 64):
        print("Sistema operativo: Linux")
    elif (ttl == 128):
        print("Sistema operativo: Windows")
    elif (ttl == 255):
        print("Sistema operativo: Mac OS")
    else:
        print("Sistema operativo: Desconocido")


if __name__ == '__main__':
    main()
