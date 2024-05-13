--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 10 — Tasks
1. Find the longest time that an employee has been at the studio
2. For each role, find the average number of years employed by employees in that role
3. Find the total number of employee years worked in each building
```
SELECT Name, MAX(Years_employed) AS Max_years_employed FROM Employees;
SELECT Role, AVG(Years_employed) AS Average_Years_employed FROM Employees GROUP BY Role;
SELECT Building, SUM(Years_employed) AS Total_years_employed FROM Employees GROUP BY Building;