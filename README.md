# Spark-Data-Analysis
## 第1章 课程准备  
  安装 VMware Workstation，SSHSecureShellClient
## 第2章 环境搭建  
  java,Scala,Hadoop,Maven,Python3,Spark  
  software文件夹  
  java环境搭建  
  ```shell    
    tar -zxvf jdk-8u91-linux-x64.tar.gz -C ~/app/
    vi ~/.bash_profile
    export JAVA_HOME=/home/hadoop/app/jdk1.8.0_91
    export PATH=$JAVA_HOME/bin:$PATH
    Esc 右下角bot模式  ：wq!
    source ~/.bash_profile
    java -version
  ```  
  scala环境搭建  
  ```shell    
    tar -zxvf scala-2.11.8.tgz -C ~/app/
    vi ~/.bash_profile
    export SCALA_HOME=/home/hadoop/app/scala-2.11.8
    export PATH=$SCALA_HOME/bin:$PATH
    Esc 右下角bot模式  ：wq!
    source ~/.bash_profile
    scala
  ```
  Hadoop环境搭建  
  1: hadoop-env.sh  
  2:core-site.xml 
  3:hdfs-site.xml  
  4:mapred-site.xml 
  4:yarn-site.xml 
  5:格式化 ./hadoop namenode -format  
  6:启动hadoop ./start-dfs.sh
  ```shell    
    tar -zxvf hadoop-2.6.0-cdh5.7.0.tar.gz -C ~/app/
    vi ~/.bash_profile
    export HADOOP_HOME=/home/hadoop/app/hadoop-2.6.0-cdh5.7.0
    export PATH=$HADOOP_HOME/bin:$PATH
    Esc 右下角bot模式  ：wq!
    source ~/.bash_profile    

    cd ~/app/hadoop-2.6.0-cdh5.7.0/etc/hadoop
    vi hadoop-env.sh
    export JAVA_HOME=/home/hadoop/app/jdk1.8.0_91
    Esc 右下角bot模式  ：wq!

    vi core-site.xml
    <configuration>
      <property>
        <name>fs.default.name</name>
        <value>hdfs://hadoop000:8020</value>
      </property>
    </configuration>
    Esc 右下角bot模式  ：wq!

    vi hdfs-site.xml
    <configuration>
      <property>
      <name>dfs.namenode.name.dir</name>
      <value>/home/hadoop/app/tmp/dfs/name</value>
      </property>

      <property>
      <name>dfs.datanode.data.dir</name>
      <value>/home/hadoop/app/tmp/dfs/data</value>
      </property>


      <property>
      <name>dfs.replication</name>
      <value>1</value>
      </property>
    </configuration>
    Esc 右下角bot模式  ：wq!

    cp mapred-site.xml.tempate mapred-site.xml
    vi mapred-site.xml
    <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
    </property>
    Esc 右下角bot模式  ：wq!

    vi yarn-site.xml
    <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
    </property>
    Esc 右下角bot模式  ：wq!

    cd ~/app/hadoop-2.6.0-cdh5.7.0/bin
    查看 /app/tmp 目录是空的
    ./hadoop namenode -format 
    Y
    查看信息 Storage directory /home/hadoop/app/tmp/dfs/name has been successfully formatted.

    cd ~/app/hadoop-2.6.0-cdh5.7.0/sbin    
    ./start-dfs.sh
    jps

    
  ```
  scala环境搭建  
  ```shell    
    tar -zxvf scala-2.11.8.tgz -C ~/app/
    vi ~/.bash_profile
    export SCALA_HOME=/home/hadoop/app/scala-2.11.8
    export PATH=$SCALA_HOME/bin:$PATH
    Esc 右下角bot模式  ：wq!
    source ~/.bash_profile
    scala
  ```
  scala环境搭建   
  ```shell    
    tar -zxvf scala-2.11.8.tgz -C ~/app/
    vi ~/.bash_profile
    export SCALA_HOME=/home/hadoop/app/scala-2.11.8
    export PATH=$SCALA_HOME/bin:$PATH
    Esc 右下角bot模式  ：wq!
    source ~/.bash_profile
    scala
  ```
  scala环境搭建   
  ```shell    
    tar -zxvf scala-2.11.8.tgz -C ~/app/
    vi ~/.bash_profile
    export SCALA_HOME=/home/hadoop/app/scala-2.11.8
    export PATH=$SCALA_HOME/bin:$PATH
    Esc 右下角bot模式  ：wq!
    source ~/.bash_profile
    scala
  ```



## 第3章 Spark Core核心RDD  
## 第4章 Spark Core RDD编程  
## 第5章 Spark运行模式  
## 第6章 Spark Core进阶  
## 第7章 Spark Core调优  
## 第8章 Spark SQL  
## 第9章 Spark Streaming  
## 第10章 Azkaban基础篇  
## 第11章 Azkaban实战篇  
## 第12章 Azkaban进阶篇  
## 第13章 项目实战  


