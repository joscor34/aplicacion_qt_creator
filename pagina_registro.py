# This Python file uses the following encoding: utf-8
import sys # <- Nos ayuda a controlar el sistema (cuando el usuario desee salir de la app lo permita)

# Nos ayudará a crear componentes de QT (gráficos)
from PySide6.QtWidgets import QApplication, QMainWindow

# Desde el archivo registro.ui quiero que importes el componente Ui_Pagina_registro

from ui_registro import Ui_Pagina_registro


from router import RouterManager

from metodos import registrar_usuario

# Con esto completamos la importación de mi apartado gráfico
# ----------------------------------------------------------




class PaginaRegistro(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.router_manager = RouterManager()

        # Le indicamos a nuestro código de donde obtendrá la parte visual
        self.ui = Ui_Pagina_registro()

        # Le decimos que se inicialice
        self.ui.setupUi(self)


        # Si el usuario presiona el botón "registro" tenemos que validar su información
        self.ui.registro.clicked.connect(self.validar_datos)

        # Si el usuario presiona el botón "Inicio sesión" mandamos a login
        self.ui.inicio_sesion.clicked.connect(self.mandar_login)


    # Esta función se va a encargar de verficar que ningún dato este faltante
    def validar_datos(self):


        # Obtenemos toda la información que el usuario haya registrado
        nombre = self.ui.texto_nombre.text()
        apellidos = self.ui.texto_apellidos.text()
        telefono = self.ui.telefono.text()
        correo = self.ui.correo.text()
        password_1 = self.ui.password_1.text()
        password_2 = self.ui.password_2.text()

        # 1.- Asegurarnos que ningún parámetro este vacío
        # 1.1.- Si alguno viene vacío, tenemos que generar un error
        if len(nombre) <= 0 or len(apellidos) <= 0 or len(telefono) <= 0 or len(password_1) <= 0:
            print('Error: Datos faltantes')
            self.ui.error.setText('Error: Datos faltantes')

        #2.- El correo que ingrese el usuario se válido
        #2.2.- Si no es válido, generamos un error
        elif '@' not in correo and '.' not in correo:
            print('Error: Correo no válido')
            self.ui.error.setText('Error: Correo no válido')

        #3.- Que ambas contraseñas coincidan
        #3.3.- Si alguna de las contraseñas no coincide tenemos que generar un error
        elif password_1 != password_2:
            print('Error: Contraseñas no coinciden')
            self.ui.error.setText('Error: Contraseñas no coinciden')

        else:
            print('Todos los datos soncorrectos :D')
            self.ui.error.setText('')

            registrar_usuario(nombre, apellidos, telefono, correo, password_1)


            # Si toda su información es válida, la guardamos en la db y lo mandamos a login
            # para que inicie sesión
            self.mandar_login()




    def mandar_login(self):
        self.router_manager.acceder_login(self)

# ----------------------------------------------------------


if __name__ == "__main__":
    # Primero creamos una aplicación (el lienzo/canva)
    app = QApplication(sys.argv)

    # Creamos la vista de esa aplicación
    widget = PaginaRegistro()

    # Mostramos a aplicación
    widget.show()

    # Salimos de la aplicación si el usuario cierra la ventana
    sys.exit(app.exec())

    # Terminamos la función


