--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 13 — Tasks
1. Add the studio's new production, Toy Story 4 to the list of movies (you can use any director) ✓
2. Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
```
INSERT INTO Movies (Id, Title, Director, Year, Length_minutes) VALUES (4, 'Toy Story 4', 'John Lasseter', 2000, 100);
INSERT INTO Boxoffice (Movie_id, Rating, Domestic_sales, International_sales) VALUES (4, 8.7, 340000000, 270000000);