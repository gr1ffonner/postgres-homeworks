-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE Student (
    student_id serial primary key,
    first_name varchar,
    last_name varchar,
    birthday date,
    phone varchar
)

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student
ADD COLUMN middle_name varchar;

-- 3. Удалить колонку middle_name
ALTER TABLE student
DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student
RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student
ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO Student (first_name, last_name, birthday, phone)
VALUES ('John', 'Doe', '2000-05-15', '+12345678901');
INSERT INTO Student (first_name, last_name, birthday, phone)
VALUES ('Alice', 'Smith', '1999-09-22', '+9876543210');
INSERT INTO Student (first_name, last_name, birthday, phone)
VALUES ('Bob', 'Johnson', '2001-03-10', '+5555555555');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
DELETE FROM student;
ALTER SEQUENCE student_student_id_seq RESTART WITH 1;