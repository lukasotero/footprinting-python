#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client
import ipaddress
import json 

def get_apache(ip_addr):

    # Constantes que vamos a utilizar
    HTTP_PORT = 80 # Puerto donde va a estar el servidor Apache, se puede cambiar
    HTTP_OK = 200
    HTTP_REDIRECT = 302
    HTTP_UNAUTHORIZED = 401

    with open('../data/versions.json') as f:
        data = json.load(f)

    try:
        cnx = http.client.HTTPConnection(ip_addr, HTTP_PORT) # Abrimos la conexion
        cnx.request('GET', '/')
        res = cnx.getresponse()
        headers = res.getheaders()
        status_cod = res.status

        print('\n+------------------------------+\n')
        print(f"Código de estado: {status_cod}\n")

        if status_cod == HTTP_OK or HTTP_REDIRECT:
            version_apache = None
            so_apache = None

            for header in headers:
                if header[0] == 'Server':
                    server = header[1]
                    print(f"Server: {server}") # Esta linea es solo para testear
                    version_apache = server.split('/')[1].split(' ')[0]
                    so_apache = server.split('(')[1].split(')')[0]
                    break

            for version in data:
                if version_apache in version:
                    so = data[version][0]
                    version_apache = version.split('-')[0]
                    break
            else:
                so = 'Sistema operativo no soportado'
                version_apache = 'Versión de Apache no soportada'

            print(f"\nSistema operativo: {so}") 

        elif status_cod == HTTP_UNAUTHORIZED:
            print('Cliente no autorizado para acceder al recurso solicitado')

        print('\n+------------------------------+')
    except http.client.HTTPException as e:
        print(f"Error en al conectarse al servidor: {e}")
    finally:
        cnx.close() # Cerramos la conexion


def verificar_ip(ip_addr):
    try:
        ip_obj = ipaddress.ip_address(ip_addr)
    except ipaddress.AddressValueError as ValueError:
        print(f"La IP es inválida: {ValueError}")


if __name__ == '__main__':
    ip_addr = input('Dirección IPv4 o IPv6 del host: ')
    verificar_ip(ip_addr)
    get_apache(ip_addr)