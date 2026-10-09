import sqlite3
from common import connect

source = connect()
try:
    for enabled in (0, 1):
        con = sqlite3.connect(":memory:")
        source.backup(con)  # Отдельная копия для каждого опыта.
        con.execute(f"PRAGMA foreign_keys = {enabled}")
        print("\nforeign_keys:", con.execute("PRAGMA foreign_keys").fetchone()[0])
        sql = "INSERT INTO students (name, group_id) VALUES (?, ?)"
        print("SQL:", sql, "Параметры:", ("Проверка связи", 999))
        try:
            con.execute(sql, ("Проверка связи", 999))
            con.commit()
            print("Добавлено. Ошибки:", con.execute("PRAGMA foreign_key_check").fetchall())
        except sqlite3.IntegrityError as error:
            con.rollback()
            print(type(error).__name__ + ":", error)
        finally:
            con.close()
    con = sqlite3.connect(":memory:")
    source.backup(con)
    con.execute("PRAGMA foreign_keys = ON")
    tests = [("NOT NULL", None, 1), ("CHECK", "   ", 1),
             ("FOREIGN KEY", "Тест", 999)]
    for label, name, group_id in tests:
        try:
            con.execute(sql, (name, group_id))
            con.commit()
        except sqlite3.IntegrityError as error:
            con.rollback()
            print(label + ":", error)
    try:
        con.execute("INSERT INTO groups (name) VALUES (?)", ("БЭИ2301",))
    except sqlite3.IntegrityError as error:
        con.rollback()
        print("UNIQUE:", error)
    con.close()
finally:
    source.close()
print("Исходная база не изменена.")
