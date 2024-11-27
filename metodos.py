import requests # <- Librería para consumir datos de internet

# This Python file uses the following encoding: utf-8

# Esta es la url a la cual vamos a estar mandando la información
url = 'https://8aca-189-193-83-212.ngrok-free.app'


# Esta función nos ayudará a crear usuarios y guardarlos en un DB
def registrar_usuario(nombre, apellido, telefono, correo, password):

    # Contendrá toda la información que voy a registrar en mi base de datos
    informacion_a_enviar = {
        'nombre': nombre + ' ' +apellido,
        'telefono': telefono,
        'mail': correo,
        'password': password
    }

    print(informacion_a_enviar)

    respuesta = requests.post(url+'/registro', data=informacion_a_enviar)

    print(respuesta.content)

def login_usuario(correo, password):

    #Este diccionario mandará toda la información la DB
    informacion_a_enviar = {
        'mail': correo,
        'password': password
    }

    print(informacion_a_enviar)

    respuesta = requests.post(url+'/login', data=informacion_a_enviar)

    print(respuesta.content)

if __name__ == "__main__":
    registrar_usuario('José', 'Esteva', '56356456356', 'jose0@correo.com', 'hola123')
#     pass
