from pathlib import Path
import argparse
import sqlite3

ROOT = Path(__file__).resolve().parent
DB = ROOT / "journal.db"
parser = argparse.ArgumentParser(description="Создать или восстановить учебную базу")
parser.add_argument("--reset", action="store_true", help="Заменить учебные таблицы исходными")
args = parser.parse_args()
existed = DB.exists()
con = sqlite3.connect(DB)
try:
    con.execute("PRAGMA foreign_keys = ON")  # До начала транзакции!
    if args.reset or not existed:
        schema = (ROOT / "schema.sql").read_text(encoding="utf-8")
        seed = (ROOT / "seed.sql").read_text(encoding="utf-8")
        # Явная транзакция нужна именно внутри executescript.
        con.executescript("BEGIN;\nDROP TABLE IF EXISTS students;\n"
                          "DROP TABLE IF EXISTS groups;\n" + schema + "\n"
                          + seed + "\nCOMMIT;")
        print("База восстановлена." if args.reset else "База создана.")
    else:
        print("База уже существует; данные сохранены.")
    print("База:", DB)
    print("foreign_keys:", con.execute("PRAGMA foreign_keys").fetchone()[0])
    for table in ("groups", "students"):
        # Имена здесь заданы программой, не пользовательским вводом.
        count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"{table}: {count}")
    for group_id in (1, 2, 3):
        count = con.execute("SELECT COUNT(*) FROM students WHERE group_id = ?",
                            (group_id,)).fetchone()[0]
        print(f"group_id={group_id}: {count}")
    errors = con.execute("PRAGMA foreign_key_check").fetchall()
    print("Ошибок связей:", len(errors))
    if errors:
        raise RuntimeError(errors)
except Exception:
    con.rollback()
    raise
finally:
    con.close()
