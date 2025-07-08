from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget

from create_zbior import ZbiorWidget
from zbior_table import ZbiorTable


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Borówka Aplikacja")
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.zbior_form = ZbiorWidget()
        layout.addWidget(self.zbior_form)

        self.table_zbior = ZbiorTable()
        layout.addWidget(self.table_zbior)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

