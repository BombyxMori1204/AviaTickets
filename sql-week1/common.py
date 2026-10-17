from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
DB = ROOT / "journal.db"


def connect():
    if not DB.exists():
        raise SystemExit("Сначала выполните python3 prepare_db.py")
    con = sqlite3.connect(DB)
    con.execute("PRAGMA foreign_keys = ON")
    assert con.execute("PRAGMA foreign_keys").fetchone()[0] == 1
    print("База:", DB)
    return con


def cell(value):
    if value is None:
        return "NULL"
    if value == "":
        return "''"
    return str(value)


def show(con, sql, params=()):
    print("\nSQL:", sql)
    print("Параметры:", params)
    cur = con.execute(sql, params)
    headers = [column[0] for column in cur.description]
    rows = [[cell(value) for value in row] for row in cur.fetchall()]
    widths = [max(len(h), *(len(r[i]) for r in rows))
              if rows else len(h) for i, h in enumerate(headers)]
    def line(row):
        return " | ".join(v.ljust(w) for v, w in zip(row, widths))
    print(line(headers))
    print("-+-".join("-" * w for w in widths))
    for row in rows:
        print(line(row))
    print("Строк в результате:", len(rows))
