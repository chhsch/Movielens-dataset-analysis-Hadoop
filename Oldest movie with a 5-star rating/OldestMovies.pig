-- Load the ratings data
ratings = LOAD '/user/maria_dev/ml-100k/u.data' AS (userID:int, movieID:int, rating:int, ratingTime:int);

-- Load the metadata for movies with specified delimiter '|'
metadata = LOAD '/user/maria_dev/ml-100k/u.item' USING PigStorage('|')
    AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);

-- Generate a name lookup table with movieID, movieTitle, and release time in Unix format
nameLookup = FOREACH metadata GENERATE movieID, movieTitle,
    ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;

-- Group the ratings by movieID
ratingsByMovie = GROUP ratings BY movieID;

-- Calculate the average rating for each movie
avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID, AVG(ratings.rating) AS avgRating;

-- Filter movies with an average rating greater than 4.0
fiveStarMovies = FILTER avgRatings BY avgRating > 4.0;

-- Join the filtered movies with the metadata
fiveStarsWithData = JOIN fiveStarMovies BY movieID, nameLookup BY movieID;

-- Order the five-star movies by release time
oldestFiveStarMovies = ORDER fiveStarsWithData BY nameLookup::releaseTime;

-- Output the result
DUMP oldestFiveStarMovies;
