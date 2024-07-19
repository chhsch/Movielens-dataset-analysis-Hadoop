from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as F

def load_movie_names():
    movie_names = {}
    with open("ml-100k/u.item", encoding="ISO-8859-1") as f:
        for line in f:
            fields = line.split('|')
            movie_names[int(fields[0])] = fields[1]
    return movie_names

def parse_input(line):
    fields = line.split()
    return Row(movieID=int(fields[1]), rating=float(fields[2]))

if __name__ == "__main__":
    # Create a SparkSession
    spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

    # Load movie names
    movie_names = load_movie_names()

    # Load and process the data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.data")
    movies = lines.map(parse_input)
    movie_dataset = spark.createDataFrame(movies)

    # Compute average rating and count for each movieID
    movie_stats = movie_dataset.groupBy("movieID").agg(
        F.avg("rating").alias("avg_rating"),
        F.count("rating").alias("rating_count")
    )

    # Get the top 10 movies with lowest average ratings
    top_ten = movie_stats.orderBy("avg_rating").limit(10).collect()

    # Print results
    for movie in top_ten:
        print(f"{movie_names[movie['movieID']]}: Average Rating = {movie['avg_rating']:.2f}, Number of Ratings = {movie['rating_count']}")

    # Stop the session
    spark.stop()