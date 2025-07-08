import sys

from PyQt6.QtWidgets import QApplication
from db import open_connection
from mainWindow import MainWindow

app = QApplication([])

if not open_connection():
    sys.exit(1)


window = MainWindow()
window.show()

app.exec()