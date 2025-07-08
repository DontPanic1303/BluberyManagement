from PyQt6.QtSql import QSqlDatabase

db = None

def open_connection() -> bool:
    global db
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("borowka.sqlite")
    return db.open()