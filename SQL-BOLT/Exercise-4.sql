--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 4 — Tasks
1. List all directors of Pixar movies (alphabetically), without duplicates
2. List the last four Pixar movies released (ordered from most recent to least)
3. List the first five Pixar movies sorted alphabetically
4. List the next five Pixar movies sorted alphabetically
```
SELECT DISTINCT Director FROM Movies ORDER BY Director ASC;
SELECT * FROM Movies ORDER BY Year DESC LIMIT 4;
SELECT * FROM Movies ORDER BY Title ASC LIMIT 5;
SELECT * FROM Movies ORDER BY Title ASC LIMIT 5 OFFSET 5;