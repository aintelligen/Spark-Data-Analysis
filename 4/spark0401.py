import sys
from pyspark import SparkConf, SparkContext
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage wordcount  <input> <output>',file=sys.stderr)
        sys.exit(-1)


    conf = SparkConf().setMaster("local[2]").setAppName("sparl041")
    sc = SparkContext(conf=conf)



    def printText():

        counts = sc.textFile(sys.argv[1]) \
            .flatMap(lambda line: line.split(" ")) \
            .map(lambda x: (x, 1)) \
            .reduceByKey(lambda a, b: a + b)\
            .saveAsTextFile(sys.argv[2])


        output = counts.collect()

        for (word, count) in output:
            print("%s: %i" % (word, count))
            
    def saveFilt():
        sc.textFile(sys.argv[1]) \
            .flatMap(lambda line: line.split("\n")) \
            .map(lambda x: (x, 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .saveAsTextFile(sys.argv[2])


    saveFilt()











    sc.stop()