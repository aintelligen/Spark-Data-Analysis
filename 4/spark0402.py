import sys

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: wordcount <input> <output>", file=sys.stderr)
        sys.exit(-1)

    conf = SparkConf()
    sc = SparkContext(conf=conf)
    # 数据文件page_view.bat
    def printResult():
        counts = sc.textFile(sys.argv[1]) \
            .flatMap(lambda x: x.split("\n")) \
            .map(lambda x: x.split(" ")) \
            .map(lambda x: (x[5], 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .map(lambda x: (x[1], x[0])) \
            .sortByKey(False) \
            .map(lambda x: (x[1], x[0])).take(5)

        for (word, count) in counts:
            print("%s: %i" % (word, count))

    def saveFile():
        sc.textFile(sys.argv[1]) \
            .flatMap(lambda x: x.split("\n")) \
            .map(lambda x: x.split(" ")) \
            .map(lambda x: (x[5], 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .map(lambda x: (x[1], x[0])) \
            .sortByKey(False) \
            .map(lambda x: (x[1], x[0])).take(5) \
            .saveAsTextFile(sys.argv[2])
    
    saveFile()
    




    sc.stop()