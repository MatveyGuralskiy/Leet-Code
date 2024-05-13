--SQL Exercises from SQL-Bolt
-------------------------------
--Created by Matvey Guralskiy
```
Exercise 14 — Tasks
1. The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
2. The year that Toy Story 2 was released is incorrect, it was actually released in 1999
3. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
```
UPDATE Movies SET Director='John Lasseter' WHERE Id = 2;
UPDATE Movies SET Year=1999 WHERE Id = 3;
UPDATE Movies SET Title='Toy Story 3', Director='Lee Unkrich' WHERE Id = 11;