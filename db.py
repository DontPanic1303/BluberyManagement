import os
import sys
import shutil
from PyQt6.QtSql import QSqlDatabase

db = None

def get_documents_db_path():
    documents_dir = os.path.join(os.path.expanduser("~"), "Documents", "Borowka")
    os.makedirs(documents_dir, exist_ok=True)
    return os.path.join(documents_dir, "borowka.sqlite")

def ensure_db_in_documents():
    target_path = get_documents_db_path()
    if not os.path.exists(target_path):
        try:
            bundled_path = os.path.join(sys._MEIPASS, "borowka.sqlite")
            shutil.copy(bundled_path, target_path)
        except Exception as e:
            print("Nie udało się skopiować bazy do Documents:", e)
    return target_path

def open_connection() -> bool:
    global db
    db = QSqlDatabase.addDatabase("QSQLITE")

    if getattr(sys, 'frozen', False):
        db_path = ensure_db_in_documents()
    else:
        db_path = os.path.abspath("borowka.sqlite")

    db.setDatabaseName(db_path)
    return db.open()
