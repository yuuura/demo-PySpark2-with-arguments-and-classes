# demo-PySpark2-with-arguments-and-classes

This demo code counts the words in the file 'book.txt' using PySpark API, then prints the result.

## Code flow
 1. 'main.py' file uses the 'SparkInit' class in the 'my_spark.py' file to create a “spark session”.  
 2. 'spark session' reads text file “book.txt” from a remote HDP server.  
 3. Using “Counter” class in the “word_count.py” file we count the words, and print the result.  
