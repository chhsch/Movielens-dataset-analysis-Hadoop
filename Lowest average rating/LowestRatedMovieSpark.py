from pyspark import SparkConf, SparkContext

def load_movie_names():
    """
    Load movie names from u.item file and return a dictionary of movie ID to movie name.
    """
    movie_names = {}
    with open("ml-100k/u.item", encoding="ISO-8859-1") as f:
        for line in f:
            fields = line.split('|')
            movie_names[int(fields[0])] = fields[1]
    return movie_names

def parse_input(line):
    """
    Parse each line of u.data and convert it to (movieID, (rating, 1.0)).
    """
    fields = line.split()
    return (int(fields[1]), (float(fields[2]), 1.0))

if __name__ == "__main__":
    # Create SparkContext
    conf = SparkConf().setAppName("WorstMovies")
    sc = SparkContext(conf=conf)

    # Load movie names
    movie_names = load_movie_names()

    # Load and process the u.data file
    lines = sc.textFile("hdfs:///user/maria_dev/ml-100k/u.data")
    movie_ratings = lines.map(parse_input)

    # Calculate average ratings
    rating_totals_and_count = movie_ratings.reduceByKey(lambda m1, m2: (m1[0] + m2[0], m1[1] + m2[1]))
    average_ratings = rating_totals_and_count.mapValues(lambda tc: tc[0] / tc[1])

    # Sort movies by average rating (ascending) and take the top 10
    worst_movies = average_ratings.sortBy(lambda x: x[1]).take(10)

    # Print results
    for movie_id, rating in worst_movies:
        print(f"{movie_names[movie_id]}: {rating:.2f}")

    # Stop SparkContext
    sc.stop()