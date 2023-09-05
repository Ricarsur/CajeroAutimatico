from PyQt5.QtWidgets import QWidget, QMessageBox,QFileDialog, QLabel, QPushButton, QFrame, QVBoxLayout, QTableWidget, QTableWidgetItem, QGridLayout,QLineEdit, QComboBox
from PyQt5.QtGui import QPalette, QPixmap, QColor, QFont, QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import Qt

class Pantalla20k (QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.retiro20k_gui()
        self.setFixedSize(400, 300)

    def retiro20k_gui(self):
        self.setStyleSheet("background-color: #202C33;")
        self.setWindowTitle("Retiros")

        retiro = 20000

        pixmap = QPixmap("image\logo falabella.png") 
        pixmap = pixmap.scaled(100, 110, Qt.KeepAspectRatio, Qt.FastTransformation)
        lbl_imagen = QLabel(self)
        lbl_imagen.setPixmap(pixmap)
        lbl_imagen.setAlignment(Qt.AlignTop | Qt.AlignHCenter)        
        lbl_imagen.setGeometry(0, 5, 420, 70)

        titulo = QLabel("Desea retirar 20.000?", self)
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
        alerta = QMessageBox()
        alerta.setWindowTitle("Transaccion aceptada")
        alerta.setText("¡Su transaccion fue aceptada, retire el dinero!")
        alerta.setIcon(QMessageBox.Information)
        alerta.exec_()
