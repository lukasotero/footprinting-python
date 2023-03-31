#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from scapy.all import *
import subprocess


def get_os(ip):
    try:
        ans, unans = sr(IP(dst=ip)/TCP(dport=80, flags="S"), timeout=10)

        if ans:
            output = subprocess.check_output(
                ['p0f', '-r', '-'], input=bytes(ans[0][1]), stderr=subprocess.PIPE)

            os = output.decode().split(';')
            os_name = os[0]
            os_version = os[1]
            os_vendor = os[2]

            print(
                f"Sistema operativo detectado: {os_name} {os_version} ({os_vendor})")
        else:
            print("No se recibió ninguna respuesta")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


ip = input("Introduce la dirección IP de la máquina que quieres escanear: ")

get_os(ip)
