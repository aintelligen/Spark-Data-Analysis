from pyspark import SparkConf, SparkContext
#创建sparkConf  设置spark相关参数信息
conf = SparkConf()

#创建SparkContext
sc = SparkContext(conf=conf)

#业务逻辑
data = [1,2,3,4,5]
distData = sc.parallelize(data)
distData.collect()
print(distData.collect())
#好的习惯
sc.stop()