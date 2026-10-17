from common import connect, show

con = connect()
try:
    if con.execute("SELECT 1 FROM students WHERE id = 61").fetchone():
        raise SystemExit("Повторный запуск: сначала python3 prepare_db.py --reset")
    print("\nДО")
    show(con, "SELECT id, name, group_id FROM students "
         "WHERE id IN (1, 61) ORDER BY id")
    with con:
        cur = con.execute("INSERT INTO students "
                          "(id, name, group_id, email) VALUES (?, ?, ?, ?)",
                          (61, "Тестовый Студент", 1, None))
        print("INSERT, изменено строк:", cur.rowcount)
    with con:
        cur = con.execute("UPDATE students SET group_id = ? WHERE id = ?", (2, 1))
        print("UPDATE, изменено строк:", cur.rowcount)
    print("\nПОСЛЕ INSERT И UPDATE")
    show(con, "SELECT id, name, group_id FROM students "
         "WHERE id IN (1, 61) ORDER BY id")
    # Тот же WHERE, что будет у DELETE: сначала проверяем выборку.
    show(con, "SELECT id, name FROM students WHERE id = ?", (61,))
    with con:
        cur = con.execute("DELETE FROM students WHERE id = ?", (61,))
        print("DELETE, изменено строк:", cur.rowcount)
    print("\nПОСЛЕ DELETE")
    show(con, "SELECT id, name, group_id FROM students "
         "WHERE id IN (1, 61) ORDER BY id")
except Exception:
    con.rollback()
    raise
finally:
    con.close()
print("Восстановите исходную группу: python3 prepare_db.py --reset")
