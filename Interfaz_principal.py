from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                             QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from otroValor import pantalla_otro
from retirar10k import Pantalla10k
from retirar20k import Pantalla20k
from retirar50k import Pantalla50k
from retirar100k import Pantalla100k


class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()
        self.setFixedSize(400, 300)
    
    def inicializar_gui(self):
        # Configuración de la ventana
        self.setStyleSheet("background-color: #202C33;")
        self.setWindowTitle("Cajero automático")

        # Contenido de la ventana
        layout_principal = QVBoxLayout(self)
        
        pixmap = QPixmap("image\logo falabella.png") 
        pixmap = pixmap.scaled(170, 170, Qt.KeepAspectRatio, Qt.FastTransformation)
        lbl_imagen = QLabel(self)
        lbl_imagen.setPixmap(pixmap)
        lbl_imagen.setAlignment(Qt.AlignTop | Qt.AlignHCenter)        
        layout_principal.addWidget(lbl_imagen)
        layout_principal.addSpacing(-50)
        lbl_titulo = QLabel('Seleccione una de las opciones', self)
        lbl_titulo.setStyleSheet("color: #FFFFFF;")
        lbl_titulo.setFont(QFont("Arial", 12, QFont.Bold))
        lbl_titulo.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout_principal.addWidget(lbl_titulo)
        layout_principal.addSpacing(-110)
        
        # Boton1 y Boton2 en el mismo QHBoxLayout
        layout_horizontal = QHBoxLayout()
                
        btn_10k = QPushButton('<--- 10.000', self)
        btn_10k.setStyleSheet("color: #FFFFFF; background-color: #00093F")
        btn_10k.setFixedSize(100, 34)
        btn_10k.clicked.connect(self.Retirar10kSeleccionado)
        
        btn_20k = QPushButton('20.0000 --->', self)
        btn_20k.setStyleSheet("color: #FFFFFF; background-color: #00093F")
        btn_20k.setFixedSize(100, 34)  
        btn_20k.clicked.connect(self.Retirar20kSeleccionado)      
        
        layout_horizontal.addWidget(btn_10k)
        
        # Agregar espaciador entre boton2 y boton1
        espaciador = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout_horizontal.addItem(espaciador)
        
        layout_horizontal.addWidget(btn_20k)
        layout_horizontal.setAlignment(Qt.AlignCenter)  # Centrar los botones
        
        layout_principal.addLayout(layout_horizontal)
        layout_principal.addSpacing(-40)

        #boton 3 y 4
        layout_horizontal3 = QHBoxLayout()
        btn_50k = QPushButton('<--- 50.000', self)
        btn_50k.setStyleSheet("color: #FFFFFF; background-color: #00093F")
        btn_50k.setFixedSize(100, 34)
        btn_50k.clicked.connect(self.Retirar50kSeleccionado)    

        btn_100k =QPushButton('100.000 --->')
        btn_100k.setStyleSheet("color: #FFFFFF; background-color: #00093F")
        btn_100k.setFixedSize(100, 34)
        btn_100k.clicked.connect(self.Retirar100kSeleccionado)    

        layout_horizontal3.addWidget(btn_50k)
        # Agregar espaciador entre boton2 y boton1
        espaciador = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout_horizontal3.addItem(espaciador)
        
        layout_horizontal3.addWidget(btn_100k)
        layout_horizontal3.setAlignment(Qt.AlignCenter)  # Centrar los botones
        
        layout_principal.addLayout(layout_horizontal3)
        layout_principal.addSpacing(-45)

        
        
        # Boton5 y boton6 en su propio QHBoxLayout
        
        layout_horizontal3 = QHBoxLayout()
        btn_otro = QPushButton('<--- Otro valor', self)
        btn_otro.setStyleSheet("color: #FFFFFF; background-color: #00093F")
        btn_otro.setFixedSize(100, 34)
        btn_otro.clicked.connect(self.retirarOtroValor)    

         

        layout_horizontal3.addWidget(btn_otro)
        
        espaciador = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout_horizontal3.addItem(espaciador)
        
        
        layout_horizontal3.setAlignment(Qt.AlignCenter)  # Centrar los botones
        
        layout_principal.addLayout(layout_horizontal3)
        layout_principal.addSpacing(-10)
        

    def Retirar10kSeleccionado(self):
        self.hide()
        self.Trae_retirar = Pantalla10k(self)
        self.Trae_retirar.show()

    def Retirar20kSeleccionado(self):
        self.hide()
        self.Trae_retirar = Pantalla20k(self)
        self.Trae_retirar.show()
    
    def Retirar50kSeleccionado(self):
        self.hide()
        self.Trae_retirar = Pantalla50k(self)
        self.Trae_retirar.show()
    
    def Retirar100kSeleccionado(self):
        self.hide()
        self.Trae_retirar = Pantalla100k(self)
        self.Trae_retirar.show()
    
    def retirarOtroValor(self):
        self.hide()
        self.Trae_retirar = pantalla_otro(self)
        self.Trae_retirar.show()

