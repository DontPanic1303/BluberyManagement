from datetime import datetime

from PyQt6.QtCore import QDate
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit


class ZbiorWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.data_label = QLabel("Data zbiorów")
        layout.addWidget(self.data_label)

        self.data_input = QDateEdit(self)
        self.data_input.setCalendarPopup(True)
        self.data_input.setDate(QDate.currentDate())
        layout.addWidget(self.data_input)

        self.kg_label = QLabel("Ilość Kg")
        layout.addWidget(self.kg_label)

        self.kg_input = QLineEdit(self)
        layout.addWidget(self.kg_input)

        self.submit_button = QPushButton("Zapisz", self)
        self.submit_button.clicked.connect(self.submit_zbior)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_zbior(self):
        data = self.data_input.date().toString("yyyy-MM-dd")
        kg = self.kg_input.text()

        try:
            float(kg)
        except:
            QMessageBox.warning(self, 'Brak danych', "Brak wprowadzonych danych do zapisania lub dane są w złej formie")
            return

        if not data or not kg:
            QMessageBox.warning(self, 'Brak danych', "Brak wprowadzonych danych do zapisania lub dane są w złej formie")
            return

        query = QSqlQuery()
        if not query.prepare("INSERT INTO Zbiory (Data, Ilosc_Kg) VALUES (:data, :kg)"):
            QMessageBox.critical(self, "Błąd SQL (prepare)", query.lastError().text())
            print("Prepare failed:", query.lastError().text())
            return

        query.bindValue(":data", data)
        query.bindValue(":kg", kg)

        print("DANE:", data, kg)
        print("QUERY (after prepare):", query.executedQuery())

        if not query.exec():
            QMessageBox.critical(self, "Błąd SQL (exec)", query.lastError().text())
            print("Exec failed:", query.lastError().text())
            return

        QMessageBox.information(self, 'Success', 'Udało się dodać')
        self.data_input.setDate(QDate.currentDate())
        self.kg_input.clear()



