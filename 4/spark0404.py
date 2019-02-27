import sys

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: avg <input>", file=sys.stderr)
        sys.exit(-1)

    conf = SparkConf()
    sc = SparkContext(conf=conf)

    ageData = sc.parallelize([20,15,21,'32',65,'54576','213123'])
    totalAge = ageData.map(lambda age:int(age)).reduce(lambda a,b:a+b)
    counts = ageData.count()
    avgAge = totalAge/counts

    print(counts)
    print(totalAge)
    print(avgAge)

    sc.stop()