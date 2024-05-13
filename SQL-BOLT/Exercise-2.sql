--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 2 — Tasks
1. Find the movie with a row id of 6
2. Find the movies released in the years between 2000 and 2010
3. Find the movies not released in the years between 2000 and 2010
4. Find the first 5 Pixar movies and their release year
```
SELECT * FROM movies WHERE Id=6;
SELECT * FROM Movies WHERE Year>=2000 AND Year<=2010;
SELECT * FROM Movies WHERE Year < 2000 OR Year > 2010;
SELECT * FROM Movies WHERE Id <= 5;