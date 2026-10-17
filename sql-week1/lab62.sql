-- Перед началом: python3 prepare_db.py --reset
-- Сохраняйте запросы в этом файле, ответы и запуск Python в README.md.
-- 1. Первые 5 студентов группы 2 по id.
-- 2. Студенты групп 1 и 3 с id >= 18; 5 строк по убыванию id.
-- 3. id от 18 до 22 включительно.
-- 4. Фамилия начинается на Иванов.
-- 5. Отдельные выборки для NULL и пустой строки email.
-- 6. Добавьте студента id=58 в группу 1; затем переведите в группу 3.
-- 7. Выведите id=58 перед удалением, удалите и проверьте отсутствие.
-- 8. Из Python выведите запрос с параметром group_id и таблицу результата.
-- 9. Восстановите базу и запустите check_db.py.
.bail on
.headers on
.mode column
.nullvalue NULL
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

.print "1. =============================="
SELECT id, name FROM students
WHERE group_id = 2
ORDER BY id
LIMIT 5;

.print "2. =============================="
SELECT id, name FROM students
WHERE group_id IN (1, 3) AND id >= 18
ORDER BY id DESC
LIMIT 5;

.print "3. =============================="      
SELECT id, name FROM students
WHERE id BETWEEN 18 AND 22;

SELECT name FROM students
WHERE name LIKE 'Иванов%';

.print "4. =============================="
SELECT email FROM students
WHERE email is NULL;

.print "5. =============================="
SELECT email FROM students
WHERE email is '';

.print "6. =============================="
INSERT INTO students (id, name, group_id, email) 
VALUES (58, 'Иванов Иван Иванович', 1, 'email@email.rom');


UPDATE students
SET group_id = 3
WHERE id = 58;

.print "7. =============================="
SELECT id, name FROM students
WHERE id = 58;

DELETE FROM students
WHERE id = 58;

SELECT id, name FROM students
WHERE id = 58;
