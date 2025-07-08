from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class PodsumowanieTable(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.podsumowanie_table = QTableWidget()
        self.podsumowanie_table.setColumnCount(4)
        self.podsumowanie_table.setHorizontalHeaderLabels(
            ['Rok', 'Zebrane kg', 'Sprzedane kg', 'Suma sprzedarzy']
        )
        layout.addWidget(self.podsumowanie_table)
        self.setLayout(layout)

        self.get_podsumowanie()

    def get_podsumowanie(self):
        self.podsumowanie_table.setRowCount(0)
        query = QSqlQuery()
        query.exec("""
                SELECT
            rok,
            SUM(zebrane_kg) AS ZebraneKg,
            SUM(sprzedane_kg) AS SprzedaneKg,
            SUM(suma_sprzedazy) AS SumaSprzedazy
        FROM (
            SELECT
                strftime('%Y', Data) AS rok,
                Ilosc_Kg AS zebrane_kg,
                0 AS sprzedane_kg,
                0 AS suma_sprzedazy
            FROM Zbiory
        
            UNION ALL
        
            SELECT
                strftime('%Y', Data) AS rok,
                0 AS zebrane_kg,
                Ilosc_Kg AS sprzedane_kg,
                Ilosc_Kg * Cena_Za_Ka AS suma_sprzedazy
            FROM Sprzedarz
        )
        GROUP BY rok
        ORDER BY rok DESC 
                   """)

        while query.next():
            rows = self.podsumowanie_table.rowCount()
            self.podsumowanie_table.setRowCount(rows + 1)
            self.podsumowanie_table.setItem(rows, 0, QTableWidgetItem(query.value(0)))
            self.podsumowanie_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.podsumowanie_table.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.podsumowanie_table.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))