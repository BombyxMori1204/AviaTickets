.bail on
.headers on
.mode column
.nullvalue NULL
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;
SELECT id, name FROM groups ORDER BY id;
SELECT id, name, group_id FROM students ORDER BY id LIMIT 5;
SELECT COUNT(*) AS students FROM students;
PRAGMA foreign_key_check;
