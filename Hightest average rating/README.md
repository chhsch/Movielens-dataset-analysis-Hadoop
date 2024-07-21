# Movie Ratings Analysis with Hive

This project uses Apache Hive to analyze movie ratings data.

## Hive Queries

```sql
-- Step 1: Create a view of average ratings
-- Ensure you have a 'ratings' table with 'movieID' and 'rating' columns
CREATE VIEW IF NOT EXISTS avgRatings AS
SELECT movieID, AVG(rating) as avgRating, COUNT(movieID) as ratingCount
FROM ratings
GROUP BY movieID
ORDER BY avgRating DESC;

-- Step 2: Query for highly-rated movies
-- Ensure you have a 'names' table with 'movieID' and 'title' columns
-- Run this query after creating the avgRatings view
SELECT n.title, ar.avgRating
FROM avgRatings ar
JOIN names n ON ar.movieID = n.movieID
WHERE ar.ratingCount > 10;