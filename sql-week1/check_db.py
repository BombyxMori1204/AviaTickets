from common import connect

con = connect()
try:
    assert con.execute("PRAGMA foreign_keys").fetchone()[0] == 1
    assert con.execute("SELECT COUNT(*) FROM groups").fetchone()[0] == 3
    assert con.execute("SELECT COUNT(*) FROM students").fetchone()[0] == 60
    for group_id in (1, 2, 3):
        assert con.execute("SELECT COUNT(*) FROM students WHERE group_id = ?",
                           (group_id,)).fetchone()[0] == 20
    assert con.execute("PRAGMA foreign_key_check").fetchall() == []
    assert con.execute("SELECT COUNT(*) FROM students WHERE email IS NULL").fetchone()[0] == 12
    assert con.execute("SELECT COUNT(*) FROM students WHERE email = ''").fetchone()[0] == 6
    print("Проверено: 3 группы, 60 студентов, 20 в каждой; NULL=12, пустых=6.")
finally:
    con.close()
