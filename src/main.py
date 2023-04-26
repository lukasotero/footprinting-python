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
<<<<<<< HEAD
        cnx = http.client.HTTPConnection(ip_addr, port) # Abrimos la conexion
        cnx.request('GET', '/') # Realiza una solicitud HTTP GET a la raíz del servidor Apache.
        res = cnx.getresponse() # Obtiene la respuesta del servidor Apache.
        headers = res.getheaders() # Obtiene los encabezados de la respuesta del servidor Apache.
        status_cod = res.status # Obtiene el código de estado de la respuesta del servidor Apache.
=======
<<<<<<< HEAD
        cnx = http.client.HTTPConnection(ip_addr, port) # Abrimos la conexion
        cnx.request('GET', '/')
        res = cnx.getresponse()
        headers = res.getheaders()
        status_cod = res.status
=======
        cnx = http.client.HTTPConnection(ip_addr, port) # Abrimos la conexión
        cnx.request('GET', '/') # Solicitud HTTP por método GET
        res = cnx.getresponse() # Guarda la respuesta de esa solicitud
        headers = res.getheaders() # Guarda los encabezados de la respuesta
        status_cod = res.status # Guarda el código de estado de la respuesta
>>>>>>> b07408fd52d4c863242cef22647741b4f8f9924f
>>>>>>> master

        print('\n+------------------------------+\n')
        print(f"Código de estado: {status_cod}\n")

        if status_cod == HTTP_OK or HTTP_REDIRECT:
            version_apache = None
            so_apache = None
<<<<<<< HEAD

            # itera sobre los encabezados de la respuesta y si encuentra el encabezado Server, extrae la versión de Apache y el sistema operativo y los guarda en las variables correspondientes.
=======
>>>>>>> master

            for header in headers:
                if header[0] == 'Server':
                    server = header[1]
                    # print(f"Server: {server}")
                    version_apache = server.split('/')[1].split(' ')[0]
                    so_apache = server.split('(')[1].split(')')[0]
                    break
<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
            
>>>>>>> b07408fd52d4c863242cef22647741b4f8f9924f
>>>>>>> master
            for version in data:
                if version_apache in version:
                    so = data[version][0]
                    version_apache = version.split('-')[0]
                    break
            
<<<<<<< HEAD
            
=======
<<<<<<< HEAD
            
=======
>>>>>>> b07408fd52d4c863242cef22647741b4f8f9924f
>>>>>>> master
            else:
                so = 'Sistema operativo no soportado'
                version_apache = 'Versión de Apache no soportada'

            print(f"Sistema operativo: {so}") 

        elif status_cod == HTTP_UNAUTHORIZED:
            print('Cliente no autorizado para acceder al recurso solicitado')

        print('\n+------------------------------+')
    except http.client.HTTPException as e:
        print(f"Error en al conectarse al servidor: {e}")
    finally:
        cnx.close() # Cerramos la conexión

<<<<<<< HEAD

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
=======
<<<<<<< HEAD

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
=======
    def verificar_ip(ip_addr):
        try:
            ip_obj = ipaddress.ip_address(ip_addr) # Si crea el objeto correctamente significa que válida la IPv4/v6
        except ipaddress.AddressValueError as ValueError:
            print(f"La IP es inválida: {ValueError}")

    if __name__ == '__main__':
        ip_addr = input('Dirección IPv4 o IPv6 del host: ')
        port = input('Puerto donde está corriendo el Apache: ')
        verificar_ip(ip_addr)
        get_apache(ip_addr, port)
>>>>>>> b07408fd52d4c863242cef22647741b4f8f9924f
>>>>>>> master
