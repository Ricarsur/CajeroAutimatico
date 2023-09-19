from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QColor, QDoubleValidator, QFont, QIcon, QIntValidator,
                         QPalette, QPixmap)
from PyQt5.QtWidgets import (QComboBox, QFileDialog, QFrame, QGridLayout,
                             QLabel, QLineEdit, QMessageBox, QPushButton,
                             QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QWidget)


class Pantalla50k (QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.retiro50k_gui()
        self.setFixedSize(400, 300)

    def retiro50k_gui(self):
        self.setStyleSheet("background-color: #202C33;")
        self.setWindowTitle("Retiros")

        retiro = 50000

        pixmap = QPixmap("image\logo falabella.png") 
        pixmap = pixmap.scaled(100, 110, Qt.KeepAspectRatio, Qt.FastTransformation)
        lbl_imagen = QLabel(self)
        lbl_imagen.setPixmap(pixmap)
        lbl_imagen.setAlignment(Qt.AlignTop | Qt.AlignHCenter)        
        lbl_imagen.setGeometry(0, 5, 420, 70)

        titulo = QLabel("Desea retirar 50.000?", self)
        titulo.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 16, QFont.Bold)
        titulo.setFont(font)
        titulo.setStyleSheet("color: #FFFFFF;")
        titulo.setGeometry(10, 50, 400, 60)

        btn_si = QPushButton('SI', self)
        btn_si.setGeometry(70, 150, 80, 50)
        btn_si.setStyleSheet(
            "QPushButton {"
            "   background-color: #188038;"
            "   border: 15px;"
            "   color: white;"
            "   padding: 10px 20px;"
            "   border-radius: 5px;"
            "   font-size: 16px;"
            "   box-shadow: 10px 5px 10px rgba(0, 0, 0, 0.5);"  # Agrega una sombra
            "}"
            "QPushButton:hover {"
            "   background-color: #105525;"  # Cambia el color al pasar el ratón
            "}"
        )
        paleta = btn_si.palette()        
        paleta.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        btn_si.clicked.connect(self.aceptar_retiro)

        btn_no = QPushButton('NO', self)
        btn_no.setGeometry(250, 150, 80, 50)
        btn_no.setStyleSheet(
            "QPushButton {"
            "   background-color: #EB0400;"
            "   border: 15px;"
            "   color: white;"
            "   padding: 10px 20px;"
            "   border-radius: 5px;"
            "   font-size: 16px;"
            "   box-shadow: 10px 5px 10px rgba(0, 0, 0, 0.5);"  # Agrega una sombra
            "}"
            "QPushButton:hover {"
            "   background-color: #9C0200;"  # Cambia el color al pasar el ratón
            "}"
        )
        paleta = btn_no.palette()        
        paleta.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        btn_no.clicked.connect(self.volver)
    def volver(self):
        self.parent.show()
        self.hide()
    def aceptar_retiro(self):
        retiro10= 10000
        retiro20= 20000
        alerta = QMessageBox()
        alerta.setWindowTitle("Transaccion aceptada")
        alerta.setText("Dinero entregado: 1 billete de "+ str(retiro10)+" y 2 billetes de "+ str(retiro20))
        alerta.setIcon(QMessageBox.Information)
        alerta.exec_()
        self.parent.show()
        self.close()
