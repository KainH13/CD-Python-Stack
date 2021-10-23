-- USE books_schema;

-- INSERT INTO authors (first_name, last_name)
-- VALUES("Jane", "Austin");
-- INSERT INTO authors (first_name, last_name)
-- VALUES("Emily", "Dickinson");
-- INSERT INTO authors (first_name, last_name)
-- VALUES("Fyodor", "Dostoevsky");
-- INSERT INTO authors (first_name, last_name)
-- VALUES("William", "Shakespeare");
-- INSERT INTO authors (first_name, last_name)
-- VALUES("Lau", "Tzu");

-- INSERT INTO books (title, num_of_pages)
-- VALUES("C Sharp", 400);
-- INSERT INTO books (title, num_of_pages)
-- VALUES("Java", 450);
-- INSERT INTO books (title, num_of_pages)
-- VALUES("Python", 300);
-- INSERT INTO books (title, num_of_pages)
-- VALUES("PHP", 350);
-- INSERT INTO books (title, num_of_pages)
-- VALUES("Ruby", 250);

-- UPDATE books SET title = "C#"
-- WHERE id = 1;

-- UPDATE authors SET first_name = "Bill"
-- WHERE id = 4;

-- INSERT INTO favorites (book_id, author_id)
-- VALUES(1, 1);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(2, 1);

-- INSERT INTO favorites (book_id, author_id)
-- VALUES(1, 2);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(2, 2);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(3, 2);

-- INSERT INTO favorites (book_id, author_id)
-- VALUES(1, 3);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(2, 3);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(3, 3);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(4, 3);

-- INSERT INTO favorites (book_id, author_id)
-- VALUES(1, 4);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(2, 4);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(3, 4);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(4, 4);
-- INSERT INTO favorites (book_id, author_id)
-- VALUES(5, 4);

-- SELECT CONCAT(authors.first_name, " ", authors.last_name) as author, books.title as favorite 
-- FROM authors
-- JOIN favorites on favorites.author_id = authors.id
-- JOIN books on books.id = favorites.book_id
-- WHERE books.id = 3;

-- SELECT CONCAT(authors.first_name, " ", authors.last_name) as author, 
-- authors.id, books.title as favorite, books.id 
-- FROM authors
-- JOIN favorites on favorites.author_id = authors.id
-- JOIN books on books.id = favorites.book_id
-- WHERE books.id = 3;

-- DELETE FROM favorites 
-- WHERE book_id = 3 AND author_id = 2;

-- INSERT INTO favorites (book_id, author_id)
-- VALUES(2, 5);

-- SELECT CONCAT(authors.first_name, " ", authors.last_name) as author, 
-- authors.id, books.title as favorite, books.id 
-- FROM authors
-- JOIN favorites on favorites.author_id = authors.id
-- JOIN books on books.id = favorites.book_id
-- WHERE authors.id = 3;

SELECT CONCAT(authors.first_name, " ", authors.last_name) as author, 
authors.id, books.title as favorite, books.id 
FROM authors
JOIN favorites on favorites.author_id = authors.id
JOIN books on books.id = favorites.book_id
WHERE books.id = 5;

-- SELECT * FROM favorites;