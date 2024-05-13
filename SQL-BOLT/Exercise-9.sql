--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 9 — Tasks
1. List all movies and their combined sales in millions of dollars
2. List all movies and their ratings in percent
3. List all movies that were released on even number years
```
SELECT Title, (Domestic_sales + International_sales) / 1000000 AS Sales_millions FROM Movies JOIN Boxoffice ON Movies.id = Boxoffice.Movie_id;
SELECT Title, Rating * 10 AS Sales_millions FROM Movies JOIN Boxoffice ON Movies.id = Boxoffice.Movie_id;
SELECT Title, Year FROM Movies WHERE Year % 2 = 0;