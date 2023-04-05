#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client
import ipaddress


SO_APACHE_DICT = {
    '2.4.48': ('Ubuntu 18.04 x64', None, 'Apache'),
    '2.4.48-openssl-1.1.1k': ('Ubuntu 18.04 x64', None, 'Apache'),
    '2.4.48-openssl-1.1.1l': ('Ubuntu 18.04 x64', None, 'Apache'),
    '2.4.49': ('Ubuntu 18.04 x64', None, 'Apache'),
    '2.4.50': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64', None, 'Apache'),
    '2.4.50-openssl-1.1.1k': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64', None, 'Apache'),
    '2.4.50-openssl-1.1.1l': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64', None, 'Apache'),
    '2.4.51': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.51-openssl-1.1.1k': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.51-openssl-1.1.1l': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.52': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.52-openssl-1.1.1k': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.52-openssl-1.1.1l': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.54': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.54-openssl-1.1.1k': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.54-openssl-1.1.1l': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.57': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64 | Ubuntu 21.10 x64', None, 'Apache'),
    '2.4.57-openssl-1.1.1k': ('Ubuntu 18.04 x64 | Ubuntu 20.04 x64', None, 'Apache'),
    '2.4.48': ('Windows 7 x86', None, 'Apache'),
    '2.4.48-openssl-1.1.1k': ('Windows 7 x86', None, 'Apache'),
    '2.4.48-openssl-1.1.1l': ('Windows 7 x86', None, 'Apache'),
    '2.4.49': ('Windows 7 x86', None, 'Apache'),
    '2.4.50': ('Windows 8 x86 | Windows 10 x86', None, 'Apache'),
    '2.4.50-openssl-1.1.1k': ('Windows 8 x86 | Windows 10 x86', None, 'Apache'),
    '2.4.50-openssl-1.1.1l': ('Windows 8 x86 | Windows 10 x86', None, 'Apache'),
    '2.4.51': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.51-openssl-1.1.1k': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.51-openssl-1.1.1l': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.52': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.52-openssl-1.1.1k': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.52-openssl-1.1.1l': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.54': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.54-openssl-1.1.1k': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.54-openssl-1.1.1l': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.57': ('Windows 8 x86 | Windows 10 x86 | Windows 11 x86', None, 'Apache'),
    '2.4.57-openssl-1.1.1k': ('Windows 8 x86 | Windows 10 x86', None, 'Apache'),
}


def get_version_apache(ip_addr):
    HTTP_PORT = 80
    HTTP_OK = 200
    HTTP_REDIRECT = 302
    HTTP_UNAUTHORIZED = 401

    try:
        cnx = http.client.HTTPConnection(ip_addr, HTTP_PORT) 
        cnx.request('GET', '/')
        res = cnx.getresponse()
        headers = res.getheaders()
        status_cod = res.status

        print('\n+----------------------------------------+\n')
        print(f"Código de estado: {status_cod}\n")

        if status_cod == HTTP_REDIRECT or HTTP_OK:
            version_apache = None
            so_apache = None

            for header in headers:
                if header[0] == 'Server':
                    server = header[1]
                    version_apache = server.split('/')[1].split(' ')[0]
                    so_apache = server.split('(')[1].split(')')[0]
                    break

            for so, versiones in SO_APACHE_DICT.items():
                v_min, v_max, so_apache_dicc = versiones
                if (so_apache_dicc == so_apache and 
                    (v_min is None or version_apache >= v_min) and
                    (v_max is None or version_apache < v_max)):
                    break
            else:
                so = 'Sistema operativo no soportado'

            print(f"\nSistema operativo: {so}") 

        elif status_cod == HTTP_UNAUTHORIZED:
            print('Cliente no autorizado para acceder al recurso solicitado')

        print('\n+----------------------------------------+')
    except http.client.HTTPException as e:
        print(f"Error en al conectarse al servidor: {e}")
    finally:
        cnx.close() 


def verificar_ip(ip_addr):
    try:
        ip_obj = ipaddress.ip_address(ip_addr)
        get_version_apache(ip_addr)
    except ipaddress.AddressValueError as e:
        print(f"La IP es inválida: {e}")


if __name__ == '__main__':
    ip_addr = input('Direccion IP/V4 del host: ')
    verificar_ip(ip_addr)