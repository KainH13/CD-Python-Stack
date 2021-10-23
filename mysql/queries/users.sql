USE users;

-- INSERT INTO users (first_name, last_name, email)
-- VALUES ("Kai", "Neuhold-Huber", "k@g.com");
-- INSERT INTO users (first_name, last_name, email)
-- VALUES ("Ariel", "Farrar", "f@g.com");
-- INSERT INTO users (first_name, last_name, email)
-- VALUES ("Dash", "Burrito", "d@g.com");

-- DELETE FROM users WHERE id IN (1, 2);

-- SELECT * FROM users
-- WHERE email = "k@g.com";

-- SELECT * FROM users
-- ORDER BY id DESC
-- LIMIT 1

-- UPDATE users SET last_name = "Pancakes"
-- WHERE id=5;

-- DELETE FROM users WHERE id=4;

SELECT * FROM users
ORDER BY first_name DESC;