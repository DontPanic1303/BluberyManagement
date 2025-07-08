from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout

from create_sprzedarz import SprzedarzWidget
from create_zbior import ZbiorWidget
from podsumowanie_table import PodsumowanieTable
from sprzedarz_table import SprzedarzTable
from zbior_table import ZbiorTable


class SprzedarzWidgetWidget:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Borówka Aplikacja")
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout_zbiory_sprzedarz = QHBoxLayout()
        layout_zbior = QVBoxLayout()
        layout_sprzedarz = QVBoxLayout()

        self.zbior_form = ZbiorWidget(self.add_zbior_to_list, self.refresh_podsumowanie)
        layout_zbior.addWidget(self.zbior_form)

        self.table_zbior = ZbiorTable()
        layout_zbior.addWidget(self.table_zbior)

        self.sprzedarz_form = SprzedarzWidget(self.add_sprzedarz_to_list, self.refresh_podsumowanie)
        layout_sprzedarz.addWidget(self.sprzedarz_form)

        self.table_sprzedarz = SprzedarzTable()
        layout_sprzedarz.addWidget(self.table_sprzedarz)

        self.table_podsumowanie = PodsumowanieTable()

        zbior_widget = QWidget()
        zbior_widget.setLayout(layout_zbior)

        sprzedarz_widget = QWidget()
        sprzedarz_widget.setLayout(layout_sprzedarz)

        layout_zbiory_sprzedarz.addWidget(zbior_widget)
        layout_zbiory_sprzedarz.addWidget(sprzedarz_widget)

        widget_zbiory_sprzedarz = QWidget()
        widget_zbiory_sprzedarz.setLayout(layout_zbiory_sprzedarz)

        layout.addWidget(widget_zbiory_sprzedarz)
        layout.addWidget(self.table_podsumowanie)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_zbior_to_list(self, data, kg):
        self.table_zbior.add_zbiory_item(data, kg)

    def add_sprzedarz_to_list(self, data, kg, cena):
        self.table_sprzedarz.add_sprzedarz_item(data, kg, cena)

    def refresh_podsumowanie(self):
        self.table_podsumowanie.get_podsumowanie()