--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Review 1 (Exercise 5) — Tasks
1. List all the Canadian cities and their populations
2. Order all the cities in the United States by their latitude from north to south
3. List all the cities west of Chicago, ordered from west to east
4. List the two largest cities in Mexico (by population)
5. List the third and fourth largest cities (by population) in the United States and their population
```
SELECT * FROM North_american_cities WHERE Country = "Canada";
SELECT * FROM North_american_cities WHERE Country = "United States" ORDER BY Latitude DESC;
SELECT * FROM North_american_cities WHERE Longitude < -87.629798 ORDER BY Longitude ASC;
SELECT * FROM North_american_cities WHERE Country = "Mexico" ORDER BY Population DESC LIMIT 2;
SELECT City, Population FROM North_american_cities WHERE Country = "United States" ORDER BY Population DESC LIMIT 2 OFFSET 2;