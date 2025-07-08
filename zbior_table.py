from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


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

        self.get_zbiory()

    def add_zbiory_item(self, data, kg):
        row_position = self.zbior_table.rowCount()
        self.zbior_table.insertRow(row_position)

        self.zbior_table.setItem(row_position, 0, QTableWidgetItem(data))
        self.zbior_table.setItem(row_position, 1, QTableWidgetItem(kg))

    def get_zbiory(self):
        query = QSqlQuery()
        query.exec("SELECT Data, Ilosc_Kg FROM Zbiory ORDER BY Data DESC")

        while query.next():
            rows = self.zbior_table.rowCount()
            self.zbior_table.setRowCount(rows + 1)
            self.zbior_table.setItem(rows, 0, QTableWidgetItem(query.value(0)))
            self.zbior_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))