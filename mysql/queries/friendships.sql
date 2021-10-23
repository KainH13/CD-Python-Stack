-- USE friendships;

-- INSERT INTO users (first_name, last_name)
-- VALUES("Milosh", "Plopski");
-- INSERT INTO users (first_name, last_name)
-- VALUES("Dashito", "Burrito");
-- INSERT INTO users (first_name, last_name)
-- VALUES("Zippy", "Dippy");
-- INSERT INTO users (first_name, last_name)
-- VALUES("Kitten", "Mitten");
-- INSERT INTO users (first_name, last_name)
-- VALUES("Mitze", "Katze");
-- INSERT INTO users (first_name, last_name)
-- VALUES("Freya", "Farrari");

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(1, 2);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(1, 4);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(1, 6);

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(2, 1);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(2, 3);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(2, 5);

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(3, 2);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(3, 5);

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(4, 3);

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(5, 1);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(5, 6);

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(6, 2);
-- INSERT INTO friendships (user_id, friend_id)
-- VALUES(6, 3);

-- SELECT users.first_name as first_name,
-- users.last_name as last_name,
-- users2.first_name as friend_first_name,
-- users2.last_name as friend_last_name
-- FROM users as users
-- JOIN friendships ON friendships.user_id = users.id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

-- SELECT users.first_name as first_name,
-- users.last_name as last_name,
-- users2.first_name as friend_first_name,
-- users2.last_name as friend_last_name
-- FROM users as users
-- JOIN friendships ON friendships.user_id = users.id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id
-- WHERE users.id = 1;

-- SELECT COUNT(id) FROM friendships;

-- SELECT users.first_name, COUNT(friendships.friend_id)
-- FROM users as users
-- JOIN friendships ON friendships.user_id = users.id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id
-- GROUP BY users.first_name
-- ORDER BY users.first_name ASC;

SELECT users2.first_name as friend_name
FROM users as users
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY users2.first_name;

-- SELECT * FROM users;