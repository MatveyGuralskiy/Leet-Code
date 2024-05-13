--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 6 — Tasks
1. Find the domestic and international sales for each movie
2. Show the sales numbers for each movie that did better internationally rather than domestically
3. List all the movies by their ratings in descending order
```
SELECT Title, Domestic_sales, International_sales FROM movies JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id;
SELECT * FROM Movies JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id WHERE International_sales > Domestic_sales;
SELECT * FROM Movies JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id ORDER BY Rating DESC;