# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_login import Ui_LoginWindow

from router import RouterManager

from metodos import login_usuario


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
        self.ui.inicio_sesion.clicked.connect(self.iniciar_sesion)


    # Este método redirige al usuario a la ventana de registro
    def mandar_a_registro(self):
        self.router_manager.acceder_registro(ventana_anterior=self)

    # Inicia sesión y manda al usuario a la página principal
    def iniciar_sesion(self):

        correo = self.ui.correo.text()
        password =  self.ui.password.text()

        login_usuario(correo, password)

        #else:
        #    self.ui.error.setText('El correo o la contraseña no coinciden :(')


# Nos ayuda a depuerar
if __name__ == "__main__":
    # Creo una variable que contenga nuestra aplicación
    app = QApplication(sys.argv)

    # Creamos un objeto que va a contener nuestra ventana
    widget = LoginWindow()

    widget.show()

    # Registramos si el usuario quiere salir de la APP
    sys.exit(app.exec())




