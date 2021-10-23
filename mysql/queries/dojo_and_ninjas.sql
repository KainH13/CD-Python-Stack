-- USE dojos_and_ninja_schema;

-- INSERT INTO dojos (name)
-- VALUES("Coding Dojo");
-- INSERT INTO dojos (name)
-- VALUES("Faltiron School");
-- INSERT INTO dojos (name)
-- VALUES("Code Academy");

-- DELETE FROM dojos WHERE id IN (1,2,3);

-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Milo", "Plopo", 1, 4);
-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Dasho", "Burrito", 1, 4);
-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Kitten", "Mitten", 12, 4);

-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Zipper", "Zippy", 1, 5);
-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Mitze", "Katze", 1, 5);
-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Speedo", "Heller", 12, 5);

-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Kaden", "Elenko", 40, 6);
-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Commander", "Shepherd", 30, 6);
-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES("Garrus", "Kerigen", 64, 6);

-- SELECT * FROM ninjas
-- WHERE dojo_id = 4;

-- SELECT * FROM ninjas
-- WHERE dojo_id = 6;

SELECT ninjas.first_name, ninjas.last_name, dojos.name
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 9;

-- SELECT * FROM ninjas;