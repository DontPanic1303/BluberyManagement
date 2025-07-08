from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget


class ZbiorTable(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.zbior_table = QTableWidget()
        self.zbior_table.setColumnCount(2)
        self.zbior_table.setHorizontalHeaderLabels(
            ['Data zbioru', 'Ilość kg']
        )
        layout.addWidget(self.zbior_table)
        self.setLayout(layout)