from common import connect, show

con = connect()
try:
    show(con, "SELECT id, name FROM groups ORDER BY id")
    show(con, "SELECT id, name, group_id FROM students ORDER BY id LIMIT 5")
    for group_id in (1, 2, 3):
        show(con, "SELECT COUNT(*) AS students FROM students WHERE group_id = ?",
             (group_id,))
finally:
    con.close()
