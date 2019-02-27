## 第3章 Spark Core核心RDD 
https://github.com/apache/spark  
Resilient Distributed Dataset (RDD)  弹性 分布式 数据集    
Represents an immutable, partitioned collection of elements that can be operated on in parallel    
不可变 并行操作  

单机存储/计算  ==> 分布式存储/计算  
1)数据的存储：切割  HDFS的Block  
2)数据的计算：分布式并行技术  MapReduce/ Spark  
3)存储+计算：HDFS/S3+MapReduce/Spark  

### RDD特性 5大特性  
Internally, each RDD is characterized by five main properties:  
 
A list of partitions    
一系列分区 构成  

A function for computing each split  
对所有分区执行相同函数  

A list of dependencies on other RDDs  
rdd1(5个partitions) (filter)==> rdd2 (map)==> rdd3  
如果rdd1 第3个partitions 数据丢失了，系统会根据（依赖） rdd2 第3个partitions计算 出 rdd1 的第3个partitions  
存在依赖关系****  

Optionally, a Partitioner for key-value RDDs (e.g. to say that the RDD is hash-partitioned) 可选 分区  
键值RDD的分区程序  

Optionally, a list of preferred locations to compute each split on (e.g. block locations for an HDFS file)  
计算每个拆分的首选位置列表  
数据在哪里就把作业调度到数据所在节点进行计算：移动数据不如移动计算（分布式存储）  


### 5大特性  对应源码  

1: partitions   
protected def getPartitions: Array[Partition]  
2：computing      
def compute(split: Partition, context: TaskContext): Iterator[T]  
3: dependencies   
protected def getDependencies: Seq[Dependency[_]] = deps  
4:  Partitioner  
val partitioner: Option[Partitioner] = None
5: preferred locations  
protected def getPreferredLocations(split: Partition): Seq[String] = Nil  


### SparkContext和SparkConf
创建SparkConf ---> 创建SparkContext --> 连接到spark '集群' (local,yarn...)  
通过SparkContext 创建RDD， 广播变量到'集群'  

### pyspark  
```shell
  cd /home/hadoop/app/spark-2.3.0-bin-2.6.0-cdh5.7.0/python  
```

启动 pyspark  
```shell
  cd /home/hadoop/app/spark-2.3.0-bin-2.6.0-cdh5.7.0/bin/pyspark  
  sc 
  <SparkContext master=local[*] appName=PySparkShell>
```  

### Spark Code 核心
http://hadoop000:4040/jobs/  
测试数据生成RDD    
Parallelized Collections  
```shell
data = [1,2,3,4,5]
distData = sc.parallelize(data,5)
distData.collect()  
```

读取文件生成RDD    
External Datasets  
If using a path on the local filesystem, the file must also be accessible at the same path on worker nodes  不建议做spark集群
```shell
发布到hdfs
 hadoop fs -put hello.txt
 sc.textFile("hdfs://hadoop000:8020/hello.txt").collect()
 distFile = sc.textFile("hdfs://hadoop000:8020/hello.txt")
 sc.wholeTextFiles("hdfs://hadoop000:8020/hello.txt").collect()  生成key-value

```
数据写进文件系统
```shell
data = [1,2,3,4,5]
distData = sc.parallelize(data)
distData.saveAsTextFile("file:///home/hadoop/data/output/")
```

### 开发pyspark 应用程序
1) IDEA pycharm
2) 新建 hello.py  运行   环境搭建
edit configurations
Evnironment variables   添加 
PYTHONPATH  D:\github\Spark-Data-Analysis\pyspark\spark\spark-2.3.3-bin-hadoop2.6\python
SPARK_HOME  D:\github\Spark-Data-Analysis\pyspark\spark\spark-2.3.3-bin-hadoop2.6\
interceptor D:\github\Spark-Data-Analysis\pyspark\spark\spark-2.3.3-bin-hadoop2.6\python\lib  2zip包


终端 192.168.10.92

```shell
mkdir ~/script
删除 master  appname
vi spark0301.py
cd app/spark-2.3.0-bin-2.6.0-cdh5.7.0/bin
提交pyspark应用程序
./spark-submit --master local[2] --name spark0301 --py /home/hadoop/script/spark0301.py  file:///home/hadoop/script/wc/*.txt


```





 