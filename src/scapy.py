#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy import *
import argparse

parse = argparse.ArgumentParse()
parse.add_argument("-r", "--rango", help="Rango de direcciones a escanear")
parse = parse.parse_args()


def ip_scan(ip):
    range_ip = ARP(pdst=ip)  # pdst = IP destino
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")  # dst = Destino MAC
    packet = broadcast/range_ip  # Unimos los dos paquetes

    # Enviamos el paquete y recibimos la respuesta
    response = srp(packet, timeout=3, verbose=False)[0]

    for n in response:
        # psrc = IP fuente | hwsrc = MAC fuente
        print(n[1].psrc + " - " + n[1].hwsrc)


def main():
    if parse.rango:
        ip_scan(parse.rango)
    else:
        print("Especifique un rango de direcciones a escanear")


if __name__ == '__main__':
    main()
