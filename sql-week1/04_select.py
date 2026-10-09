from common import connect, show

con = connect()
try:
    queries = [
        ("SELECT id, name FROM students WHERE group_id = ? ORDER BY id LIMIT 3", (2,)),
        ("SELECT id, name FROM students WHERE id BETWEEN ? AND ? ORDER BY id", (18, 22)),
        ("SELECT id, name FROM students WHERE name LIKE ? ORDER BY id", ("Иванов%",)),
        ("SELECT id, name FROM students "
         "WHERE group_id IN (1, 3) AND id <= 42 "
         "ORDER BY id DESC LIMIT 5", ()),
    ]
    for sql, params in queries:
        show(con, sql, params)
finally:
    con.close()
