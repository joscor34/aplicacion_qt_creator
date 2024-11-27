# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Pagina_registro(object):
    def setupUi(self, Pagina_registro):
        if not Pagina_registro.objectName():
            Pagina_registro.setObjectName(u"Pagina_registro")
        Pagina_registro.resize(800, 745)
        self.centralwidget = QWidget(Pagina_registro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 0, 151, 121))
        self.label.setStyleSheet(u"font: 24pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 160, 91, 20))
        self.texto_nombre = QLineEdit(self.centralwidget)
        self.texto_nombre.setObjectName(u"texto_nombre")
        self.texto_nombre.setGeometry(QRect(80, 190, 261, 28))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 240, 63, 20))
        self.texto_apellidos = QLineEdit(self.centralwidget)
        self.texto_apellidos.setObjectName(u"texto_apellidos")
        self.texto_apellidos.setGeometry(QRect(80, 270, 261, 28))
        self.telefono = QLineEdit(self.centralwidget)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setGeometry(QRect(80, 350, 261, 28))
        self.correo = QLineEdit(self.centralwidget)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(80, 430, 261, 28))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 400, 63, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 320, 91, 20))
        self.password_2 = QLineEdit(self.centralwidget)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(80, 590, 261, 28))
        self.password_1 = QLineEdit(self.centralwidget)
        self.password_1.setObjectName(u"password_1")
        self.password_1.setGeometry(QRect(80, 510, 261, 28))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 480, 91, 20))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 560, 181, 20))
        self.registro = QPushButton(self.centralwidget)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(490, 270, 151, 91))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(420, 410, 161, 20))
        self.inicio_sesion = QPushButton(self.centralwidget)
        self.inicio_sesion.setObjectName(u"inicio_sesion")
        self.inicio_sesion.setGeometry(QRect(590, 410, 91, 29))
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(450, 210, 231, 20))
        self.error.setStyleSheet(u"color: rgb(255, 0, 0)")
        Pagina_registro.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Pagina_registro)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        Pagina_registro.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Pagina_registro)
        self.statusbar.setObjectName(u"statusbar")
        Pagina_registro.setStatusBar(self.statusbar)

        self.retranslateUi(Pagina_registro)

        QMetaObject.connectSlotsByName(Pagina_registro)
    # setupUi

    def retranslateUi(self, Pagina_registro):
        Pagina_registro.setWindowTitle(QCoreApplication.translate("Pagina_registro", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Pagina_registro", u"Registro", None))
        self.label_2.setText(QCoreApplication.translate("Pagina_registro", u"Nombre(s)", None))
        self.label_3.setText(QCoreApplication.translate("Pagina_registro", u"Apellidos", None))
        self.label_4.setText(QCoreApplication.translate("Pagina_registro", u"Correo", None))
        self.label_5.setText(QCoreApplication.translate("Pagina_registro", u"Telefono", None))
        self.label_6.setText(QCoreApplication.translate("Pagina_registro", u"Contrase\u00f1a", None))
        self.label_7.setText(QCoreApplication.translate("Pagina_registro", u"Verificar  contrase\u00f1a", None))
        self.registro.setText(QCoreApplication.translate("Pagina_registro", u"Registrarme", None))
        self.label_8.setText(QCoreApplication.translate("Pagina_registro", u"\u00bfYa tienes una cuenta? ", None))
        self.inicio_sesion.setText(QCoreApplication.translate("Pagina_registro", u"Inicia sesi\u00f3n", None))
        self.error.setText("")
    # retranslateUi

