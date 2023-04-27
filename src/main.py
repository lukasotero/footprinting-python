#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client
import ipaddress
import json

def get_apache(ip_addr, port):

    # Constantes que vamos a utilizar
    HTTP_OK = 200
    HTTP_REDIRECT = 302
    HTTP_UNAUTHORIZED = 401

    with open('../data/versions.json') as f:
        data = json.load(f)

    try:
        cnx = http.client.HTTPConnection(ip_addr, port) # Abrimos la conexión
        cnx.request('GET', '/') # Solicitud HTTP por método GET
        res = cnx.getresponse() # Guarda la respuesta de esa solicitud
        headers = res.getheaders() # Guarda los encabezados de la respuesta
        status_cod = res.status # Guarda el código de estado de la respuesta

        print('\n+------------------------------+\n')
        print(f"Código de estado: {status_cod}")

        if status_cod == HTTP_OK or HTTP_REDIRECT:
            server = None

            for header in headers:
                if header[0] == 'Server':
                    server = header[1]
                    dist_so = server.split('(')[1].split(')')[0]
                    print(f"Server: {server}")
                    break

            for version in data:
                if dist_so in version:
                    so = data[version][0]
                    break
            
            else:
                so = 'Sistema operativo no agregado al diccionario'

            print(f"\nSistema operativo: {so}") 

        elif status_cod == HTTP_UNAUTHORIZED:
            print('Cliente no autorizado para acceder al recurso solicitado')

        print('\n+------------------------------+')
    except http.client.HTTPException as e:
        print(f"Error en al conectarse al servidor: {e}")
    finally:
        cnx.close() # Cerramos la conexión


def verificar_ip(ip_addr):
    try:
        ip_obj = ipaddress.ip_address(ip_addr)
    except ipaddress.AddressValueError as ValueError:
        print(f"La IP es inválida: {ValueError}")


if __name__ == '__main__':
    ip_addr = input('Dirección IPv4 o IPv6 del host: ')
    port = input('Puerto donde está corriendo el Apache: ')
    verificar_ip(ip_addr)
    get_apache(ip_addr, port)
