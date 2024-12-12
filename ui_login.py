# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, -10, 411, 181))
        self.label.setStyleSheet(u"font: 36pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 160, 63, 20))
        self.correo = QLineEdit(self.centralwidget)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(200, 190, 391, 28))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 240, 211, 20))
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(200, 270, 391, 28))
        self.password.setEchoMode(QLineEdit.Password)
        self.inicio_sesion = QPushButton(self.centralwidget)
        self.inicio_sesion.setObjectName(u"inicio_sesion")
        self.inicio_sesion.setGeometry(QRect(310, 330, 141, 41))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 470, 131, 20))
        self.registro = QPushButton(self.centralwidget)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(380, 470, 131, 29))
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(280, 400, 221, 20))
        self.error.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.cargando = QLabel(self.centralwidget)
        self.cargando.setObjectName(u"cargando")
        self.cargando.setGeometry(QRect(350, 390, 50, 50))
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Inicio de sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a", None))
        self.inicio_sesion.setText(QCoreApplication.translate("LoginWindow", u"Iniciar sesi\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"\u00bfNo tienes cuenta?", None))
        self.registro.setText(QCoreApplication.translate("LoginWindow", u"Crea una ahora", None))
        self.error.setText("")
        self.cargando.setText("")
    # retranslateUi

