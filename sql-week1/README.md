# SQL — первая неделя

Две лекции по 90 минут и две отдельные лабораторные по 90 минут.
Все имена и адреса вымышлены. 3 группы: БЭИ2301, БЭИ2302, БЭИ2303;
по 20 студентов, всего 60. Данные обеих лекций одинаковые.

## Debian Linux

```bash
sudo apt update
sudo apt install python3 sqlite3 unzip
unzip sql-week1.zip
cd sql-week1
python3 prepare_db.py --reset
python3 check_db.py
sqlite3 journal.db < console.sql
```

Python использует стандартный модуль sqlite3, pip и Tkinter не нужны.
Версии Python и консольной SQLite могут различаться: `python3 --version`,
`python3 -c "import sqlite3; print(sqlite3.sqlite_version)"`, `sqlite3 --version`.

## Подключение из консоли

```text
sqlite3 journal.db
.databases
.tables
.schema students
.headers on
.mode column
.nullvalue NULL
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;
SELECT id, name FROM groups ORDER BY id;
.quit
```

Ожидается foreign_keys=1, группы 1–3 и указанный файл journal.db.
PRAGMA выполняйте при КАЖДОМ подключении, до транзакции.
Включение проверки в консоли не включает её в Python.

## Структура, заполнение и повторный запуск

`schema.sql` создаёт таблицы; `seed.sql` содержит все 60 записей.
Исходные данные загружаются сначала в groups, затем в students.
`python3 prepare_db.py` создаёт отсутствующую базу; существующую не заполняет повторно.
`python3 prepare_db.py --reset` заменяет учебные таблицы и восстанавливает
исходные данные. Закройте другие подключения во время восстановления.
Скрипт работает только с journal.db рядом с собой; не передавайте ему рабочую базу.
При ошибке создание/восстановление откатывается. Транзакции подробно разберём на следующей неделе.

Для ручного создания ОТДЕЛЬНОЙ базы в корне комплекта:

```text
sqlite3 lab61.db
.bail on
PRAGMA foreign_keys = ON;
.read schema.sql
.read seed.sql
SELECT COUNT(*) FROM students;
.quit
```

Ожидается 60. Повторный `.read schema.sql` даёт ошибку существующей таблицы,
повторный `.read seed.sql` — ошибку первичного ключа: это не способ восстановления.
Вызов `.read` и команды с точкой принадлежат консольной программе, а не SQL.
Для нового чистого ручного опыта используйте другое имя файла базы.

## Демонстрации в терминале

| Команда | Что показываем | Изменяет journal.db |
|---|---|---|
| `python3 01_tables.py` | Группы, строки, 20 студентов в каждой | Нет |
| `python3 02_constraints.py` | Внешние ключи OFF/ON и ошибки ограничений | Нет, отдельные копии в памяти |
| `python3 03_types.py` | typeof и VARCHAR без ограничения длины | Нет |
| `python3 04_select.py` | Фильтры, сортировка, параметры | Нет |
| `python3 05_null.py` | NULL, пустая строка, IS NULL | Нет |
| `python3 06_changes.py` | INSERT, перевод id=1 в группу 2, DELETE id=61 | Да |
| `python3 prepare_db.py --reset` | Восстановление 3/60/20 | Да |
| `python3 check_db.py` | Проверка исходного состояния | Нет |

Все скрипты выводят путь к базе; запросы — SQL, параметры, заголовки и таблицу.
NULL отображается как NULL, пустая строка как ''. Скрипт изменений показывает
состояние до/после и число затронутых строк. После него обязательно выполните reset.
Для capture: `python3 04_select.py > select-output.txt`; ошибки stderr можно
сохранить вместе: `python3 04_select.py > select-output.txt 2>&1`.
Базовые проверки: groups=3, students=60, group_id 1/2/3 по20,
NULL email=12, пустых email=6, foreign_key_check не возвращает строк.

## Лабораторные и следующий шаг

`lab61.sql`, `lab62.sql` — задания. `teacher/` предназначена преподавателю;
при выдаче студентам уберите эту папку. Презентации и конспекты находятся
в отдельных файлах комплекта. JOIN, GROUP BY, транзакции и обзор psycopg
для PostgreSQL будут на второй неделе SQL; здесь используем sqlite3 и `?`.

## Документация

- https://www.sqlite.org/cli.html
- https://www.sqlite.org/foreignkeys.html
- https://www.sqlite.org/datatype3.html
- https://www.sqlite.org/lang_expr.html
- https://docs.python.org/3/library/sqlite3.html
