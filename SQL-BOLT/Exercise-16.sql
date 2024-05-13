--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 16 — Tasks
Create a new table named Database with the following columns:
1. Name A string (text) describing the name of the database
2. Version A number (floating point) of the latest version of this database
3. Download_count An integer count of the number of times this database was downloaded
This table has no constraints.
```
CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);