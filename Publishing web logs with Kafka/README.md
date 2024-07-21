# Kafka Log Processing

This project demonstrates how to use Apache Kafka for log processing in a Hortonworks sandbox environment.

## Setup and Execution

```bash
# Copy configuration files
cp connect-standalone.properties ~/
cp connect-file-sink.properties ~/
cp connect-file-source.properties ~/

# Edit configuration files
cd ~
vi connect-standalone.properties
# Change bootstrap.servers to sandbox.hortonworks.com:6667

vi connect-file-sink.properties
# Change file=/home/maria_dev/logout.txt
# Set topics=log-test

vi connect-file-source.properties
# Change file=/home/maria_dev/access_log_small.txt
# Set topics=log-test

# Download sample log file
wget http://media.sundog-soft.com/hadoop/access_log_small.txt
less access_log_small.txt

result:
66.249.75.159 - - [29/Nov/2015:03:50:05 +0000] "GET /robots.txt HTTP/1.1" 200 55 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.75.168 - - [29/Nov/2015:03:50:06 +0000] "GET /blog/ HTTP/1.1" 200 8083 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
185.71.216.232 - - [29/Nov/2015:03:53:15 +0000] "POST /wp-login.php HTTP/1.1" 200 1691 "http://nohatenews.com/wp-login.php" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
54.165.199.171 - - [29/Nov/2015:04:32:27 +0000] "GET /sitemap_index.xml HTTP/1.0" 200 592 "-" "W3 Total Cache/0.9.4.1"
54.165.199.171 - - [29/Nov/2015:04:32:27 +0000] "GET /post-sitemap.xml HTTP/1.0" 200 2502 "-" "W3 Total Cache/0.9.4.1"

# In a separate console:
# Create Kafka topic
./kafka-topics.sh --create --zookeeper sandbox-hdp:2181 --replication-factor 1 --partitions 1 --topic log-test

# Start Kafka consumer
./kafka-console-consumer.sh --bootstrap-server sandbox.hortonworks.com:6667 --topic log-test --zookeeper localhost:2181

# In the original console:
# Run Kafka Connect
cd /usr/hdp/current/kafka-broker/bin
./connect-standalone.sh ~/connect-standalone.properties ~/connect-file-source.properties ~/connect-file-sink.properties