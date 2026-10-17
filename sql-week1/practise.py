from pathlib import Path
import argparse
from random import choice
import sqlite3

ROOT = Path(__file__).resolve().parent
DB = ROOT / "lab62.db"
last_names = ["Иванов", "Петров", "Ватутин", "Грибоедов", "Патронов", "Васнецов", "Васельцов", "Весельчак", "Бодров"]
first_names = ["Александр", "Кирилл", "Мустафа", "Муххамад", "Денис", "Виктор", "Стас", "Владислав"]
con = sqlite3.connect(DB)
con.execute("PRAGMA foreign_keys = ON") 
con.executescript("DROP TABLE IF EXISTS students;")
con.executescript("DROP TABLE IF EXISTS groups;")

con.executescript("""CREATE TABLE groups 
    (id INTEGER PRIMARY KEY, Group_name TEXT NOT NULL UNIQUE
    CHECK(length(trim(Group_name)) > 0)
    );""")
con.executescript("""CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL
    CHECK(length(trim(name)) > 0), group_id INTEGER NOT NULL, email TEXT,
    FOREIGN KEY (group_id) REFERENCES groups(id)
    );""")

for i in range(1, 4):
    con.execute("INSERT INTO groups (Group_name) VALUES (?)", (f"Группа {i}",))
    for j in range(1, 20):
        con.execute("INSERT INTO students (name, group_id, email) VALUES (?, ?, ?)",
                    (f"{choice(last_names)} {choice(first_names)}", i, f"student{j}@group{i}.com"))

con.commit()
cursor = con.execute("SELECT id, name, email FROM students")
print(f"{'id':<5} | {'name':<20} | {'email':<30}")
print("-" * 60)

for student_id, student_name, student_email in cursor.fetchall():
    print(f"{student_id:<5} | {student_name:<20} | {student_email:<30}")

        