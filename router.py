# Este archivo nos ayudará a manejar las rutas
from PySide6.QtCore import QObject


class RouterManager(QObject):
    def __init__(self):

        # La ventana actual nos ayudará a determinar desde que ventana venimos
        self.ventana_actual = None


    def acceder_login(self, ventana_anterior=None):
        from pagina_login import LoginWindow

        # Creamos un objeto de la ventana nueva que queremos mostrar
        self.ventana_actual = LoginWindow()

        # En ese objeto aplicamos el método show para que se muestre
        self.ventana_actual.show()

        # Cerramos la ventana anterior
        ventana_anterior.close()


    def acceder_registro(self, ventana_anterior=None):
        from pagina_registro import PaginaRegistro


        self.ventana_actual = PaginaRegistro()
        self.ventana_actual.show()

        # Cerramos la ventana anterior
        ventana_anterior.close()

    def acceder_principal(self, ventana_anterior=None, nombre_usuario=""):
        from pagina_principal import Pagina_principal

        self.ventana_actual = Pagina_principal(nombre_usuario=nombre_usuario)
        self.ventana_actual.show()


        # Cerramos la ventana anterior
        ventana_anterior.close()
