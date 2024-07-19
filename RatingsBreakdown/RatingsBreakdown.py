from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_get_ratings,
                reducer=self.reducer_count_ratings
            )
        ]

    def mapper_get_ratings(self, _, line):
        # Split each line of the input data into components
        userID, movieID, rating, timestamp = line.split('\t')
        # Yield the rating as the key and 1 as the value
        yield rating, 1

    def reducer_count_ratings(self, key, values):
        # Sum all the values for each rating key
        yield key, sum(values)

if __name__ == '__main__':
    RatingsBreakdown.run()
