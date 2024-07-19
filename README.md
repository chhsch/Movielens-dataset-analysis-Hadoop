# Hadoop Project with MRJob and Nano on Mac

This project demonstrates the setup and execution of a MapReduce job using Hadoop, MRJob, and Nano on a Mac environment. Below are the detailed steps to install the necessary components and run the example script.

## Prerequisites

- Hadoop Distribution (HDP 2.5)
- Python
- Pip

## Set Up Stack

### Hortonworks Data Platform (HDP)

#### Install HDP Sandbox

1. Download and install HDP sandbox version 2.3 or later. The sandbox includes various components such as Hive and Sqoop.
2. Follow the instructions provided by Hortonworks to set up the sandbox environment.

## Load Dataset into HDFS

1. Create a directory in HDFS:
    ```bash
    hadoop fs -mkdir ml-100k
    ```
2. Verify the directory creation:
    ```bash
    hadoop fs -ls
    ```
3. Download the dataset:
    ```bash
    wget http://media.sundog-soft.com/hadoop/ml-100k/u.data
    ```
4. Copy the dataset from the local file system to HDFS:
    ```bash
    hadoop fs -copyFromLocal u.data ml-100k/u.data
    ```

## Installation Steps

### Install Pip

1. Navigate to the yum repositories directory:
    ```bash
    cd /etc/yum.repos.d
    ```
2. Copy the sandbox repository file to a temporary location:
    ```bash
    cp sandbox.repo /tmp
    ```
3. Remove the sandbox repository file:
    ```bash
    rm sandbox.repo
    ```
4. Go to the home directory:
    ```bash
    cd ~
    ```
5. Install Python pip:
    ```bash
    yum install python-pip
    ```

### Install MRJob

1. Install the Google API Python client:
    ```bash
    pip install google-api-python-client==1.6.4
    ```
2. Install MRJob:
    ```bash
    pip install mrjob==0.5.11
    ```

### Install Nano

1. Install the Nano text editor:
    ```bash
    yum install nano
    ```