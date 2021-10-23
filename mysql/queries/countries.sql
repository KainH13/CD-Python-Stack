-- USE world;

-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- JOIN languages ON languages.country_id = countries.id
-- WHERE languages.language = "Slovene";

-- SELECT countries.name, COUNT(cities.id) as num_cities
-- FROM countries
-- JOIN cities ON cities.country_id = countries.id
-- GROUP BY countries.name
-- ORDER BY num_cities DESC;

-- SELECT cities.name
-- FROM cities
-- JOIN countries ON countries.id = cities.country_id
-- WHERE countries.name = "Mexico" AND cities.population > 500000;

-- SELECT countries.name, languages.language, languages.percentage
-- FROM languages
-- JOIN countries ON countries.id = languages.country_id
-- WHERE languages.percentage > 89
-- ORDER BY languages.percentage DESC;

-- SELECT name, surface_area, population
-- FROM countries
-- WHERE surface_area < 501 AND population > 100000

-- SELECT name, government_form, capital, life_expectancy
-- FROM countries
-- WHERE government_form = "Constitutional Monarchy"
-- AND capital > 200
-- AND life_expectancy > 75;

-- SELECT countries.name as country_name,
-- cities.name as city_name,
-- cities.district as district,
-- cities.population as population
-- FROM countries
-- JOIN cities ON cities.country_id = countries.id
-- WHERE cities.district = "Buenos Aires" AND cities.population > 500000;

-- SELECT region, COUNT(id) as countries
-- FROM countries
-- GROUP BY region
-- ORDER BY countries DESC;

-- SELECT region, name, population, surface_area
-- FROM countries
-- WHERE region = "Australia and New Zealand"\

SELECT name, population, surface_area
FROM countries
WHERE population > 400000
ORDER BY surface_area;
 
-- SELECT * FROM countries
-- LIMIT 10;