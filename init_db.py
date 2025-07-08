import sqlite3

def execute_query(db_path, query):
    try:
        # Połączenie z bazą danych
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Wykonanie zapytania
        cursor.execute(query)

        # Jeśli zapytanie zwraca dane (np. SELECT)
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            conn.commit()
            print("Query executed successfully.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Przykładowe użycie
    db_file = "borowka.sqlite"  # ścieżka do pliku bazy danych
    sql_query = """
    delete from Zbiory

"""  # przykładowe zapytanie

    execute_query(db_file, sql_query)
