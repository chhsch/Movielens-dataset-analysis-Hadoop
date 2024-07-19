# MovieLens 100K Data Analysis

This project contains two PySpark applications that analyze movie ratings from the MovieLens 100K dataset. One script finds the worst-rated movies, while the other identifies the least popular (lowest-rated) movies with additional statistics.

## Prerequisites

- Python 3.6+
- Apache Spark 2.4+
- PySpark (for the Popular Movies script)
- MovieLens 100K dataset

## Setup

1. Ensure you have Python and Apache Spark installed on your system.
2. If using the Popular Movies script, make sure PySpark is also installed.
3. Download the MovieLens 100K dataset and place the `u.data` file in the HDFS directory: `hdfs:///user/maria_dev/ml-100k/`.
4. Place the `u.item` file in the `ml-100k` directory in your local project folder.

## Scripts

### 1. Worst Movies Analyzer (worst_movies.py)

This script finds the 10 worst-rated movies based on average ratings.


#### How it works
1. Loads movie names from the `u.item` file.
2. Reads the `u.data` file from HDFS.
3. Calculates the average rating for each movie.
4. Sorts movies by average rating in ascending order.
5. Displays the 10 worst-rated movies with their ratings.

#### Output Format

### 2. Popular Movies Analyzer (popular_movies.py)

This script finds the 10 least popular movies based on average ratings and includes the number of ratings received.

#### Output Format

## Key Differences Between Scripts

1. **Implementation**: 
   - Worst Movies uses RDD operations.
   - Popular Movies uses DataFrame operations.

2. **Output**:
   - Worst Movies shows only the movie name and average rating.
   - Popular Movies includes the number of ratings for each movie.

3. **Libraries**:
   - Worst Movies uses basic PySpark (SparkConf, SparkContext).
   - Popular Movies uses PySpark SQL (SparkSession, functions).

4. **Performance**:
   - Popular Movies may be more efficient for large datasets due to DataFrame optimizations.

5. **Flexibility**:
   - Popular Movies script is easier to extend for more complex analyses due to the use of DataFrames.



