from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class SprzedarzTable(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.sprzedarz_table = QTableWidget()
        self.sprzedarz_table.setColumnCount(3)
        self.sprzedarz_table.setHorizontalHeaderLabels(
            ['Data zbioru', 'Ilość kg', 'Cena za kg']
        )
        layout.addWidget(self.sprzedarz_table)
        self.setLayout(layout)

        self.get_sprzedarz()

    def add_sprzedarz_item(self, data, kg, cena):
        row_position = self.sprzedarz_table.rowCount()
        self.sprzedarz_table.insertRow(row_position)

        self.sprzedarz_table.setItem(row_position, 0, QTableWidgetItem(data))
        self.sprzedarz_table.setItem(row_position, 1, QTableWidgetItem(kg))
        self.sprzedarz_table.setItem(row_position, 2, QTableWidgetItem(cena))

    def get_sprzedarz(self):
        query = QSqlQuery()
        query.exec("SELECT Data, Ilosc_Kg, Cena_Za_Ka FROM Sprzedarz ORDER BY Data DESC")

        while query.next():
            rows = self.sprzedarz_table.rowCount()
            self.sprzedarz_table.setRowCount(rows + 1)
            self.sprzedarz_table.setItem(rows, 0, QTableWidgetItem(query.value(0)))
            self.sprzedarz_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.sprzedarz_table.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))