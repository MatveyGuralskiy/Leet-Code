--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 8 — Tasks
1. Find the name and role of all employees who have not been assigned to a building ✓
2. Find the names of the buildings that hold no employees
```
SELECT Name, Role FROM Employees WHERE Building IS NULL;
SELECT DISTINCT Building_name FROM Buildings LEFT JOIN Employees ON Building_name = Building WHERE Role IS NULL;