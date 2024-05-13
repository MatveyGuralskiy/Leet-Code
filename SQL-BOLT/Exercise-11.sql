--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 11 — Tasks
1. Find the number of Artists in the studio (without a HAVING clause)
2. Find the number of Employees of each role in the studio
3. Find the total number of years employed by all Engineers
```
SELECT Role, COUNT(*) AS Total_artists FROM Employees WHERE Role = 'Artist';
SELECT Role, COUNT(*) AS Total_employees FROM Employees GROUP BY Role;
SELECT Name, SUM(Years_employed) FROM Employees WHERE Role = 'Engineer';