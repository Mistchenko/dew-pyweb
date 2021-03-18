-- Вставка
INSERT INTO blog_note
    (title, message, date_add, public, author_id)
VALUES
    ('Заголовок первый SQL 1', 'Текст SQL 1', '2000-01-01 01:21:00', 0, 1),
    ('Заголовок второй SQL 2', 'Текст SQL 2', '2000-01-02 01:21:00', 0, 2),
    ('Заголовок третий SQL 3', 'Текст SQL 2', '2000-01-02 01:21:00', 0, 2),
    ('Заголовок четвертый SQL 4', 'Текст SQL 2', '2000-01-02 01:21:00', 0, 2),
    ('Заголовок пятый SQL 5', 'Текст SQL 2', '2000-01-02 01:21:00', 0, 2),
    ('Заголовок шестой SQL 6', 'Текст SQL 2', '2000-01-02 01:21:00', 0, 2)
;

-- Изменение записи (строки) по ID
UPDATE blog_note
SET
    message='Новый текст'
WHERE id=45
;

-- Изменение нескольких записей для одного автора
UPDATE blog_note
SET public=1
WHERE author_id=2
;

-- Удаление записи
DELETE FROM blog_note; --WHERE id in (1,2,3);

-- Выборка записей
SELECT * FROM blog_note WHERE author_id=2
;

SELECT * FROM blog_note
LEFT JOIN auth_user AS au on au.id = blog_note.author_id
;

SELECT bn.title, au.username FROM blog_note AS bn
JOIN auth_user AS au on au.id = bn.author_id
;

SELECT bn.title, au.username FROM blog_note AS bn
JOIN auth_user AS au on au.id = bn.author_id
WHERE au.username='admin'
;

SELECT bn.title, au.username FROM blog_note AS bn
JOIN auth_user AS au on au.id = bn.author_id
order by bn.public and au.username
;

SELECT bn.title, au.username FROM blog_note AS bn
JOIN auth_user AS au on au.id = bn.author_id
order by bn.public and au.username
LIMIT 3
OFFSET 3
;

SELECT bn.date_add, bn.title, au.username FROM blog_note AS bn
JOIN auth_user AS au on au.id = bn.author_id
WHERE public=0
order by bn.date_add DESC, au.username ASC
LIMIT 3
;

SELECT bn.title, au.username FROM blog_note AS bn
JOIN auth_user AS au on au.id = bn.author_id
WHERE title LIKE '%шестой%'
;

-- Функции
SELECT count(*) AS count FROM blog_note WHERE title LIKE '%шестой%';

-- Анализ производительности
EXPLAIN SELECT * FROM blog_note