from datetime import datetime

from PyQt6.QtCore import QDate, QLocale
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit


class SprzedarzWidget(QWidget):
    def __init__(self, on_submit_callback, on_submit_refresh_podsumowanie):
        super().__init__()
        self.on_submit_callback = on_submit_callback
        self.on_submit_refresh_podsumowanie = on_submit_refresh_podsumowanie

        layout = QVBoxLayout()

        self.data_label = QLabel("Data sprzedarzy")
        layout.addWidget(self.data_label)

        self.data_input = QDateEdit(self)
        self.data_input.setLocale(QLocale(QLocale.Language.Polish))
        self.data_input.setCalendarPopup(True)
        self.data_input.setDate(QDate.currentDate())
        layout.addWidget(self.data_input)

        self.kg_label = QLabel("Ilość Kg")
        layout.addWidget(self.kg_label)

        self.kg_input = QLineEdit(self)
        layout.addWidget(self.kg_input)

        self.cena_label = QLabel("Cena")
        layout.addWidget(self.cena_label)

        self.cena_input = QLineEdit(self)
        layout.addWidget(self.cena_input)

        self.submit_button = QPushButton("Zapisz", self)
        self.submit_button.clicked.connect(self.submit_sprzedarz)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_sprzedarz(self):
        data = self.data_input.date().toString("yyyy-MM-dd")
        kg = self.kg_input.text()
        cena = self.cena_input.text()

        try:
            float(kg)
            float(cena)
        except:
            QMessageBox.warning(self, 'Brak danych', "Brak wprowadzonych danych do zapisania lub dane są w złej formie")
            return

        if not data or not kg or not cena:
            QMessageBox.warning(self, 'Brak danych', "Brak wprowadzonych danych do zapisania lub dane są w złej formie")
            return

        query = QSqlQuery()
        if not query.prepare("INSERT INTO Sprzedarz (Data, Ilosc_Kg, Cena_Za_Ka) VALUES (:data, :kg, :cena)"):
            QMessageBox.critical(self, "Błąd SQL (prepare)", query.lastError().text())
            print("Prepare failed:", query.lastError().text())
            return

        query.bindValue(":data", data)
        query.bindValue(":kg", kg)
        query.bindValue(":cena", cena)

        if not query.exec():
            QMessageBox.critical(self, "Błąd SQL (exec)", query.lastError().text())
            print("Exec failed:", query.lastError().text())
            return

        self.on_submit_callback(data, kg, cena)
        self.on_submit_refresh_podsumowanie()
        QMessageBox.information(self, 'Success', 'Udało się dodać')
        self.data_input.setDate(QDate.currentDate())
        self.kg_input.clear()
        self.cena_input.clear()



