from common import connect, show

con = connect()
try:
    show(con, "SELECT id, email FROM students WHERE id IN (1, 5, 7) ORDER BY id")
    for condition in ("email = NULL", "email IS NULL", "email = ''"):
        show(con, "SELECT id, email FROM students WHERE " + condition +
             " ORDER BY id LIMIT 4")
finally:
    con.close()
