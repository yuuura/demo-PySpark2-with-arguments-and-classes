import my_spark
import word_count

# Creating a spark session into a global var
my_spark.SparkInit().init()

# By using global var 'sc', we will read a text file 'book.txt', which is in our hadoop cluster
# 'path_in_hadoop_cluster' - The path where our file 'book.txt' is located in hadoop cluster
lines = my_spark.sc.sparkContext.textFile("/path_in_hadoop_cluster/book.txt")

# Using class 'Counter' we will count words from 'book.txt' file
# and print the result
print word_count.Counter(lines).count_words()


