# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_login import Ui_LoginWindow

from router import RouterManager

from metodos import login_usuario
from metodos import cargar_token
from metodos import decode_token

import time
import asyncio
from qasync import asyncSlot


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Inicializamos un par de atribútos
        # Contendrá la Ui de nuestra ventana
        self.ui = Ui_LoginWindow()

        # Configurar la venta que vamos a mostrar
        self.ui.setupUi(self)

        self.router_manager = RouterManager()


        # Cuando el botón "registro" sea precionado ejecutamos el mandar a registro
        self.ui.registro.clicked.connect(self.mandar_a_registro)

        # Iniciamos sesión con el usuario
        self.ui.inicio_sesion.clicked.connect(self.manejar_inicio_asincrono)


    # Este método redirige al usuario a la ventana de registro
    def mandar_a_registro(self):
        self.router_manager.acceder_registro(ventana_anterior=self)

    # Este manejador nos permite utilizar funciones asíncronas
    @asyncSlot()
    async def manejar_inicio_asincrono(self):
        await self.iniciar_sesion()


    # Inicia sesión y manda al usuario a la página principal
    async def iniciar_sesion(self):

## await

        correo = self.ui.correo.text()
        password =  self.ui.password.text()

        self.ui.cargando.setText('Cargando...')

        respuesta = await login_usuario(correo, password)

        self.ui.cargando.setText('')

        mi_token = cargar_token()


        print(f'El token para este punto es: {mi_token}')

        datos_token = decode_token(mi_token)

        print(respuesta)

        if 'Token' in respuesta:
            self.router_manager.acceder_principal(self, datos_token['sub'])

        else:
            self.ui.error.setText('El correo o la contraseña no coinciden :(')


# Nos ayuda a depuerar
if __name__ == "__main__":
    # Creo una variable que contenga nuestra aplicación
    app = QApplication(sys.argv)

    # Creamos un objeto que va a contener nuestra ventana
    widget = LoginWindow()

    widget.show()

    # Registramos si el usuario quiere salir de la APP
    sys.exit(app.exec())




