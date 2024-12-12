import requests # <- Librería para consumir datos de internet
import json
import os
import jwt
import datetime
import asyncio
import httpx
import aiofiles

# This Python file uses the following encoding: utf-8

# Esta es la url a la cual vamos a estar mandando la información
url = 'https://5f26-189-250-213-163.ngrok-free.app'


def eliminar_token():
    with open('token.txt', 'w') as file:
        #Dentro de ese archivo, se guarde el token
        file.write('')


# Determine la caducidad de mi token
def token_es_valido(expiracion):

    fecha_expiracion = datetime.datetime.fromtimestamp(expiracion)


    return fecha_expiracion > datetime.datetime.now()

    # Si es mayor (True), significa que el token es válido
    # Si es menor (False), significa que mi token ya expiró



# Una función para poder decodificar el token
def decode_token(token):

    # Verificando si existe un token que decodificar
    if token:
        # Decodificamos el payload del token
        payload = jwt.decode(token, options={'verify_signature': False})

        # Imprimimos el payload decodificado
        return payload

    return None



# Una función donde cargue el archivo txt y obtenga el token
def cargar_token():
    # Primero comprobamos si el archivo "token.txt" existe

    if os.path.exists('token.txt'):
        # El archivo existe

        # Abrimos el archivo y retornamos su contenido (el token)
        with open('token.txt', 'r') as file:

            contenido = file.read()
            # Compara si mi el archivo donde se guarda el token está vacío
            if len(contenido) == 0:
                return None

            return contenido

    else:
        # El archivo no existe entonces retornamos algo vacío
        return None

# Esta función crea un archivo txt donde se almacena el token
async def crear_archivo_token(token):
    # Abra un archivo y si no existe, que lo cree
    async with aiofiles.open('token.txt', 'w') as file:
        #Dentro de ese archivo, se guarde el token
        await file.write(token)


# Esta función nos ayudará a crear usuarios y guardarlos en un DB
def registrar_usuario(nombre, apellido, telefono, correo, password):

    # Contendrá toda la información que voy a registrar en mi base de datos
    informacion_a_enviar = {
        'nombre': nombre + ' ' +apellido,
        'telefono': telefono,
        'correo': correo,
        'password': password
    }

    print(informacion_a_enviar)

    respuesta = requests.post(url+'/registro', data=informacion_a_enviar)

    respuesta_string = respuesta.content.decode('utf-8')

    respuesta_diccionario = json.loads(respuesta_string)

    return respuesta_diccionario



async def login_usuario(correo, password):

    #Este diccionario mandará toda la información la DB
    informacion_a_enviar = {
        'correo': correo,
        'password': password
    }

    print(informacion_a_enviar)

    async with httpx.AsyncClient() as cliente:

        respuesta = await cliente.post(url+'/login', data=informacion_a_enviar)

    respuesta_string = respuesta.content.decode('utf-8')

    respuesta_diccionario = json.loads(respuesta_string)

    if 'Token' in respuesta_diccionario:

        # Se crea el archivo "token.txt" y dentro se guarda el token generado
        await crear_archivo_token(respuesta_diccionario['Token'])


    return respuesta_diccionario

if __name__ == "__main__":
    mi_token_actual = cargar_token()

    # Decodificamos la información del token
    payload_token = decode_token(mi_token_actual)

    valido = token_es_valido(payload_token['exp'])

    print(valido)
#     pass
