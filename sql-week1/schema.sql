CREATE TABLE groups (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
        CHECK(length(trim(name)) BETWEEN 1 AND 50)
);
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
        CHECK(length(trim(name)) BETWEEN 1 AND 50),
    group_id INTEGER NOT NULL,
    email TEXT,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);
