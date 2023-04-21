#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos  http.client ipaddress json 

import http.client
import ipaddress
import json 

def get_apache(ip_addr, port):

    # Constantes que vamos a utilizar
    HTTP_OK = 200 # Representa el código de estado HTTP para una respuesta exitosa.
    HTTP_REDIRECT = 302 # Representa el código de estado HTTP para una redirección.
    HTTP_UNAUTHORIZED = 401 # Representa el código de estado HTTP para una solicitud no autorizad

    # Abre el archivo versions.json que contiene información sobre las versiones de Apache y lo carga en la variable data utilizando la función json.load().
    with open('../data/versions.json') as f:
        data = json.load(f)

    # Crea una conexión HTTP con el servidor Apache utilizando la dirección IP ip_addr y el puerto HTTP_PORT.
    try:
        cnx = http.client.HTTPConnection(ip_addr, port) # Abrimos la conexion
        cnx.request('GET', '/') # Realiza una solicitud HTTP GET a la raíz del servidor Apache.
        res = cnx.getresponse() # Obtiene la respuesta del servidor Apache.
        headers = res.getheaders() # Obtiene los encabezados de la respuesta del servidor Apache.
        status_cod = res.status # Obtiene el código de estado de la respuesta del servidor Apache.

        print('\n+------------------------------+\n')
        print(f"Código de estado: {status_cod}\n")

        # Verifica si el código de estado es HTTP_OK o HTTP_REDIRECT.

        if status_cod == HTTP_OK or HTTP_REDIRECT:
            version_apache = None
            so_apache = None

            # itera sobre los encabezados de la respuesta y si encuentra el encabezado Server, extrae la versión de Apache y el sistema operativo y los guarda en las variables correspondientes.

            for header in headers:
                if header[0] == 'Server':
                    server = header[1]
                    # print(f"Server: {server}")
                    version_apache = server.split('/')[1].split(' ')[0]
                    so_apache = server.split('(')[1].split(')')[0]
                    
                    # if server == None:
                    #     print(f'No hay un servidor Apache corriendo en el puerto {port}')

                    break
            
            # Itera sobre las versiones de Apache almacenadas en data y si encuentra una que coincide con 
            for version in data:
                if version_apache in version:
                    so = data[version][0]
                    version_apache = version.split('-')[0]
                    break
            
                
            # Si no encuentra ninguna versión de Apache que coincida con version_apache, establece los valores de so y version_apache en mensajes de error.
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

    # Recibe como parámetro una dirección IP y se encarga de verificar si la dirección es una dirección IP válida
    def verificar_ip(ip_addr):
        try:
            ip_obj = ipaddress.ip_address(ip_addr)
    # Si la dirección IP no es válida, se captura la excepción AddressValueError y se imprime un mensaje de error indicando que la dirección es inválida.
        except ipaddress.AddressValueError as ValueError:
            print(f"La IP es inválida: {ValueError}")

    # De solicita al usuario que ingrese la dirección IP y el puerto donde se encuentra corriendo el servidor Apache
    if __name__ == '__main__':
        ip_addr = input('Dirección IPv4 o IPv6 del host: ')
        port = input('Puerto donde está corriendo el Apache: ')
        verificar_ip(ip_addr)
        get_apache(ip_addr, port)