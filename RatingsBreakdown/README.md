## Mechanism for MapReduce

The MapReduce mechanism for this project is as follows:

1. **Map** each input line to (rating, 1).
2. **Reduce** each rating with the sum of all the 1’s.

```python
def mapper(self, _, line):
    (user_id, movie_id, rating, timestamp) = line.split('\t')
    yield rating, 1
    
def reducer(self, key, values):
    yield key, sum(values)
```
## Data Files and Script

1. Download the dataset and the script:
    ```bash
    wget http://media.sundog-soft.com/hadoop/ml-100k/u.data
    wget http://media.sundog-soft.com/hadoop/RatingsBreakdown.py
    ```

2. Run the MapReduce job using the script:
    ```bash
    python RatingsBreakdown.py -r hadoop --hadoop-streaming-jar /user/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data
    ```

## Usage

The provided script, `RatingsBreakdown.py`, can be used to analyze the dataset stored in HDFS. Ensure that the Hadoop streaming JAR path is correctly specified when running the script.


 