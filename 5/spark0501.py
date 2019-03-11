import sys, time
from pyspark import SparkConf, SparkContext
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage wordcount <input> <output>',file=sys.stderr)
        sys.exit(-1)


    conf = SparkConf().setMaster("local[2]").setAppName("sparl041")
    sc = SparkContext(conf=conf)


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

    def getPaths():
        now = int(time.time())
        timeArray = time.localtime(now)
        paths = time.strftime("%Y-%m-%d_%H-%M-%S", timeArray)
        return '/'+paths
      # page_view.txt
    def saveFile():
        print(sys.argv[1],sys.argv[2]+getPaths())

        # sc.textFile(sys.argv[1]) \
        #   .flatMap(lambda x: x.split("\n")) \
        #   .map(lambda x: x.split(" ")) \
        #   .map(lambda x: (x[5], 1)) \
        #   .reduceByKey(lambda a, b: a + b) \
        #   .map(lambda x: (x[1], x[0])) \
        #   .sortByKey(False) \
        #   .map(lambda x: (x[1], x[0]))\
        #   .saveAsTextFile(sys.argv[2]+getPaths())
        
        sc.textFile(sys.argv[1]) \
          .flatMap(lambda x: x.split("\n")) \
          .map(lambda x: x.split(" ")) \
          .saveAsTextFile(sys.argv[2])



    printResult()
    saveFile()











    sc.stop()