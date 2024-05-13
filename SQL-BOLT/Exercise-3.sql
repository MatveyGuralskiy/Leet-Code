--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 3 — Tasks
1. Find all the Toy Story movies 
2. Find all the movies directed by John Lasseter
3. Find all the movies (and director) not directed by John Lasseter
4. Find all the WALL-* movies
```
SELECT * FROM Movies WHERE Title LIKE "%Toy Story%";
SELECT * FROM Movies WHERE Director LIKE "%John Lasseter%";
SELECT * FROM Movies WHERE Director NOT LIKE "%John Lasseter%";
SELECT * FROM Movies WHERE Title LIKE "%WALL-%";