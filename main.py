import sys
from PyQt5.QtWidgets import QApplication
from Interfaz_principal import Inicio

if __name__ == '__main__':
    app = QApplication([])
    ventana = Inicio()
    ventana.show()
    sys.exit(app.exec_())