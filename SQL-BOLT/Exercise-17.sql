--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 17 — Tasks
1. Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
2. Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
```
ALTER TABLE Movies ADD COLUMN Aspect_ratio FLOAT DEFAULT 5.12;
ALTER TABLE Movies ADD COLUMN Language TEXT DEFAULT English;