--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 7 — Tasks
1. Find the list of all buildings that have employees
2. Find the list of all buildings and their capacity
3. List all buildings and the distinct employee roles in each building (including empty buildings)
```
SELECT DISTINCT Building FROM Employees;
SELECT * FROM Buildings;
SELECT DISTINCT Building_name, Role FROM Buildings LEFT JOIN Employees ON Buildings.Building_name = Employees.Building;