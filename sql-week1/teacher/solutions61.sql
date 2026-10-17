PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;
.read schema.sql
.read seed.sql
SELECT COUNT(*) AS groups_count FROM groups;
SELECT COUNT(*) AS students_count FROM students;
SELECT COUNT(*) AS group_1 FROM students WHERE group_id = 1;
SELECT COUNT(*) AS group_2 FROM students WHERE group_id = 2;
SELECT COUNT(*) AS group_3 FROM students WHERE group_id = 3;
PRAGMA foreign_key_check;
-- Ошибки выполняйте по одной; намеренно не включено .bail on.
INSERT INTO students (name, group_id) VALUES (NULL, 1);
INSERT INTO students (name, group_id) VALUES ('   ', 1);
INSERT INTO students (name, group_id) VALUES ('Тест', 999);
INSERT INTO groups (name) VALUES ('БЭИ2301');
