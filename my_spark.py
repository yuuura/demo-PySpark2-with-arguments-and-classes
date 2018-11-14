from pyspark.sql import SparkSession


class SparkInit:
    def init(self):
        global sc
        sc = SparkSession.builder.getOrCreate()
