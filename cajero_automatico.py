from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QColor, QDoubleValidator, QFont, QIcon, QIntValidator,
                         QPalette)
from PyQt5.QtWidgets import (QComboBox, QFileDialog, QFrame, QGridLayout,
                             QLabel, QLineEdit, QMessageBox, QPushButton,
                             QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QWidget)


class OtroVlr_code:
    @staticmethod
    def ejecutar_codigo (cantidad):
        billete10 = 0
        billete20 = 0
        billete50 = 0
        billete100 = 0
        cantidadRestante = int(cantidad)
        modulo = 0

        modulo = cantidadRestante % 10000

        if modulo == 0:
            while cantidadRestante != 0:
                if cantidadRestante >= 10000:
                    cantidadRestante -= 10000
                    billete10 += 1
                if cantidadRestante >= 20000:
                    cantidadRestante -= 20000
                    billete20 += 1
                if cantidadRestante >= 50000:
                    cantidadRestante -= 50000
                    billete50 += 1
                if cantidadRestante >= 100000:
                    cantidadRestante -= 100000
                    billete100 += 1
                if cantidadRestante >= 20000:
                    cantidadRestante -= 20000
                    billete20 += 1
                if cantidadRestante >= 50000:
                    cantidadRestante -= 50000
                    billete50 += 1
                if cantidadRestante >= 100000:
                    cantidadRestante -= 100000
                    billete100 += 1
                if cantidadRestante >= 50000:
                    cantidadRestante -= 50000
                    billete50 += 1
                if cantidadRestante >= 100000:
                    cantidadRestante -= 100000
                    billete100 += 1
                if cantidadRestante >= 100000:
                    cantidadRestante -= 100000
                    billete100 += 1

            resultado = f"10k: {billete10}\n20k: {billete20}\n50k: {billete50}\n100k: {billete100}"
            alerta = QMessageBox()
            alerta.setWindowTitle("Transaccion aceptada")
            alerta.setText("Dinero entregado: "+ str(resultado))
            alerta.setIcon(QMessageBox.Information)
            alerta.exec_()
            print(resultado)
        else:
            resultado = "El monto ingresado no es válido"
            print(resultado)


