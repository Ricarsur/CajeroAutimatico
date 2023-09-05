import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class CajeroAutomatico(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cajero Automático")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Ingrese la cantidad a retirar:", self)
        self.label.move(20, 20)

        self.input_box = QLineEdit(self)
        self.input_box.move(20, 50)

        self.result_label = QLabel("", self)
        self.result_label.move(20, 100)

        self.button = QPushButton("Retirar", self)
        self.button.move(20, 150)
        self.button.clicked.connect(self.calcular_billetes)

    def calcular_billetes(self):
        cantidad = int(self.input_box.text())
        denominaciones = [100000, 50000, 20000, 10000]
        resultado = {}

        for denom in denominaciones:
            cantidad_de_billetes = cantidad // denom
            if cantidad_de_billetes > 0:
                resultado[denom] = cantidad_de_billetes
                cantidad %= denom

        mensaje = ""
        for denom, cantidad_de_billetes in resultado.items():
            mensaje += f"{cantidad_de_billetes}({denom//1000}k) + "

        mensaje = mensaje[:-2]  # Eliminar el último "+"
        self.result_label.setText(f"Billetes a entregar: {mensaje}")

def main():
    app = QApplication(sys.argv)
    ventana = CajeroAutomatico()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
