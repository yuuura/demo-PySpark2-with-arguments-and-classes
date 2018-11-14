# demo-PySpark2-with-arguments-and-classes

This demo code counts the words in the file 'book.txt' using PySpark API, then prints the result.

## Code flow
'main.py' script uses the 'SparkInit' class in the 'my_spark.py' script to create a “spark session”.
After creating a 'spark session', the “main.py” script reads “book.txt” from a remote HDP server.
Finally, “main.py” script uses the “Counter” class in the “word_count.py” script to count words.

