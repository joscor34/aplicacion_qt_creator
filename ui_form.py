# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Pagina_principal(object):
    def setupUi(self, Pagina_principal):
        if not Pagina_principal.objectName():
            Pagina_principal.setObjectName(u"Pagina_principal")
        Pagina_principal.resize(629, 499)
        Pagina_principal.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.centralwidget = QWidget(Pagina_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 141, 81))
        self.label.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.cerrar_sesion = QPushButton(self.centralwidget)
        self.cerrar_sesion.setObjectName(u"cerrar_sesion")
        self.cerrar_sesion.setGeometry(QRect(470, 400, 131, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 331, 20))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        Pagina_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Pagina_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 629, 25))
        Pagina_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Pagina_principal)
        self.statusbar.setObjectName(u"statusbar")
        Pagina_principal.setStatusBar(self.statusbar)

        self.retranslateUi(Pagina_principal)

        QMetaObject.connectSlotsByName(Pagina_principal)
    # setupUi

    def retranslateUi(self, Pagina_principal):
        Pagina_principal.setWindowTitle(QCoreApplication.translate("Pagina_principal", u"Pagina_principal", None))
        self.label.setText(QCoreApplication.translate("Pagina_principal", u"Principal", None))
        self.cerrar_sesion.setText(QCoreApplication.translate("Pagina_principal", u"Cerrar sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("Pagina_principal", u"Bienvenido: Nombre", None))
    # retranslateUi

