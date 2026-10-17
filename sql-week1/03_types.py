import sqlite3
from common import show

con = sqlite3.connect(":memory:")
try:
    con.execute("CREATE TABLE sample (value INTEGER, label VARCHAR(3))")
    con.executemany("INSERT INTO sample VALUES (?, ?)",
                    [("42", "длинная строка"), ("текст", "abc")])
    show(con, "SELECT value, typeof(value) AS stored_type, label FROM sample")
finally:
    con.close()
