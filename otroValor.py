from PyQt5.QtWidgets import QWidget,QFileDialog, QLabel, QPushButton, QFrame, QVBoxLayout, QTableWidget, QTableWidgetItem, QGridLayout,QLineEdit, QComboBox
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtCore import Qt

class pantalla_otro(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.otro_retiro_gui()
        self.setFixedSize(400, 300)
    
    def otro_retiro_gui(self):
        self.setStyleSheet("background-color: #202C33;")
        self.setWindowTitle("Retiros")

        titulo = QLabel("Area de retiros", self)
        titulo.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 16, QFont.Bold)
        titulo.setFont(font)
        titulo.setStyleSheet("color: #FFFFFF;")
        titulo.setGeometry(10, 0, 400, 60)

        btn_salir = QPushButton('Volver', self)
        btn_salir.setGeometry(5, 15, 50, 30)
        paleta = btn_salir.palette()
        btn_salir.setStyleSheet("background-color: #0D1333;")
        paleta.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        btn_salir.setPalette(paleta)
        btn_salir.setStyleSheet("{ border-radius: 50px; }")
        btn_salir.clicked.connect(self.volver_principal)

        linea_separadora = QFrame(self)
        linea_separadora.setGeometry(0, 50, 800, 15)
        linea_separadora.setFrameShape(QFrame.HLine)
        linea_separadora.setFrameShadow(QFrame.Sunken)
        linea_separadora.setStyleSheet("color: gray;")

        lbl_titulovr = QLabel('Digite el valor a retirar', self)
        lbl_titulovr.setStyleSheet("color: #FFFFFF;")
        lbl_titulovr.setFont(QFont("Arial", 12, QFont.Bold))
        lbl_titulovr.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        lbl_titulovr.setGeometry(80, 90, 260, 60)

        self.valor_sacar = QLineEdit(self)
        self.valor_sacar.setAlignment(Qt.AlignCenter)
        self.valor_sacar.setStyleSheet("color: white;")
        self.valor_sacar.setFont(QFont("Arial", 14, QFont.Bold))
        self.valor_sacar.setGeometry(145, 125, 120, 35)
        validator = QIntValidator(self)
        self.valor_sacar.setValidator(validator)

        self.enviar = QPushButton("Sacar", self)
        self.enviar.setGeometry(145, 180, 120, 25)
        self.enviar.setStyleSheet("background-color: #00093F;color: white;")
        paleta = self.enviar.palette()
        paleta.setColor(QPalette.ButtonText, QColor(255, 255, 255))

    def volver_principal(self):
        self.parent.show()
        self.hide()