--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 15 — Tasks
1. This database is getting too big, lets remove all movies that were released before 2005.
2. Andrew Stanton has also left the studio, so please remove all movies directed by him.
```
DELETE FROM Movies WHERE Year < 2005;
DELETE FROM Movies WHERE Director = 'Andrew Stanton';