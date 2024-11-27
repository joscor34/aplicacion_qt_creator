# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Pagina_principal

from router import RouterManager


class Pagina_principal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1.- Hace referencia al UI de nuestra página
        # Le indica de donde ve a sacar el apartado gráfico
        self.ui = Ui_Pagina_principal()

        # De ese apartado gráfico lo inicializamos
        self.ui.setupUi(self)

        # Creamos un objeto de tipo RouterManager
        self.router_manager = RouterManager()

        self.ui.cerrar_sesion.clicked.connect(self.cerrar_sesion)

    def cerrar_sesion(self):

        # Esta línea de código nos ayuda a enviar al usuario al login
        self.router_manager.acceder_login(ventana_anterior=self)


# Determinar si el usuario está ejecutando este archivo.
if __name__ == "__main__":

    # Primero creamos una aplicación (el lienzo/canva)
    app = QApplication(sys.argv)

    # Creamos la vista de esa aplicación
    widget = Pagina_principal()

    # Mostramos a aplicación
    widget.show()

    # Salimos de la aplicación si el usuario cierra la ventana
    sys.exit(app.exec())

    # Terminamos la función
