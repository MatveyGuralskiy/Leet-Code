--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 12 — Tasks
1. Find the number of movies each director has directed
2. Find the total domestic and international sales that can be attributed to each director
```
SELECT DISTINCT Director, COUNT(*) AS Total_movies FROM Movies GROUP BY Director;
SELECT Director, SUM(Domestic_sales + International_sales) AS Total_sales FROM Movies JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id GROUP BY Director;