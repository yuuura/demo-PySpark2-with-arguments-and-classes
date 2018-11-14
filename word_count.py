class Counter:

    def __init__(self, lines):
        self.lines = lines

    def count_words(self):
        return self.lines.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b).count()
