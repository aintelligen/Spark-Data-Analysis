## 第4章 Spark Core RDD编程  
 本章将针对RDD中常用的算子进行详细案例讲解，并进行综合案例实战  
### RDD常用操作  
 RDD Operations
  transformations: create a new dataset from an existing one    
    rddb = rdda.map(...).collect()
    lazy(*****)，不会立刻计算，记住关系，当遇到action时才计算
    map /filter /group /by  /distinct

  actions:  return a value to the driver program after running a computation on the dataset  
    rddb = fn(rdda)  
    count reduce collect ....
  
  transformations are lazy ,nothind happends until an action is called
  action triggers the computions;
  action reuturns values to driver or writes data to external storage

词频案例：spark0401.py  
  1:input n文件  后缀名  
  2：flatMap  map  reduceByKey  
```shell
cd app/spark-2.3.0-bin-2.6.0-cdh5.7.0/bin

./spark-submit --master local[2] --name spark0402 /home/hadoop/script/spark0402.py  file:///home/hadoop/script/wc/*.txt

```

TopN   
  flatMap  map  reduceByKey  sortByKey









