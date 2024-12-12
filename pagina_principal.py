# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Pagina_principal

from router import RouterManager

from metodos import cargar_token
from metodos import decode_token
from metodos import token_es_valido
from metodos import eliminar_token

from qasync import QEventLoop
import asyncio

class Pagina_principal(QMainWindow):
    def __init__(self, nombre_usuario="", parent=None):
        super().__init__(parent)

        # 1.- Hace referencia al UI de nuestra página
        # Le indica de donde ve a sacar el apartado gráfico
        self.ui = Ui_Pagina_principal()


        # Atributo que almacene el nombre el usuario
        self.nombre_usuario = nombre_usuario

        # De ese apartado gráfico lo inicializamos
        self.ui.setupUi(self)

        # Creamos un objeto de tipo RouterManager
        self.router_manager = RouterManager()

        self.ui.label_nombre.setText(f'Bienvenido {self.nombre_usuario}')

        self.ui.cerrar_sesion.clicked.connect(self.cerrar_sesion)



    def cerrar_sesion(self):


        eliminar_token()
        # Esta línea de código nos ayuda a enviar al usuario al login
        self.router_manager.acceder_login(ventana_anterior=self)


# Determinar si el usuario está ejecutando este archivo.
if __name__ == "__main__":


    # Tenemos que determinar el estado de mi token
    token_actual = cargar_token()

    # Decodificamos la información del token
    payload_token = decode_token(token_actual)

    if payload_token:
        valido = token_es_valido(payload_token['exp'])

    else:
        valido = None

    router_manager = RouterManager()


    # Primero creamos una aplicación (el lienzo/canva)
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    # Crear el entorno asíncrono para nuestra app
    asyncio.set_event_loop(loop)

    # Creamos la vista de esa aplicación
    widget = Pagina_principal()

    # Mostramos a aplicación
    #widget.show()


    if valido:

        # Si el token es válido el administrador de rutas hace que el usuario
        # acceda a la página principal
        print('Se carga la pagina inicio')

        print(payload_token)

        nombre = payload_token['sub']

        router_manager.acceder_principal(widget, nombre)
    else:
        # Si el token es inválido el administrador de rutas hace que el usuario
        # acceda a la página login
        print('Se carga login')
        router_manager.acceder_login(widget)


    with loop:
        loop.run_forever()

    # Salimos de la aplicación si el usuario cierra la ventana
    sys.exit(app.exec())
