# Spark-Data-Analysis
[Python3实战Spark大数据分析及调度](https://coding.imooc.com/class/chapter/249.html#Anchor)

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
    Esc 右下角bot模式  :wq!
    source ~/.bash_profile
    java -version
  ```  
  scala环境搭建  
  ```shell    
    tar -zxvf scala-2.11.8.tgz -C ~/app/
    vi ~/.bash_profile
    export SCALA_HOME=/home/hadoop/app/scala-2.11.8
    export PATH=$SCALA_HOME/bin:$PATH
    Esc 右下角bot模式  :wq!
    source ~/.bash_profile
    scala
  ```
  Hadoop环境搭建  
  1:hadoop-env.sh  
  2:core-site.xml  
  3:hdfs-site.xml  
  4:mapred-site.xml   
  4:yarn-site.xml   
  5:./hadoop namenode -format    
  6:修改hosts
  7:./start-dfs.sh   
  8:./start-yarn.sh
  ```shell    
    tar -zxvf hadoop-2.6.0-cdh5.7.0.tar.gz -C ~/app/
    vi ~/.bash_profile
    export HADOOP_HOME=/home/hadoop/app/hadoop-2.6.0-cdh5.7.0
    export PATH=$HADOOP_HOME/bin:$PATH
    Esc 右下角bot模式  :wq!
    source ~/.bash_profile    

    cd ~/app/hadoop-2.6.0-cdh5.7.0/etc/hadoop
    vi hadoop-env.sh
    export JAVA_HOME=/home/hadoop/app/jdk1.8.0_91
    Esc 右下角bot模式  :wq!

    vi core-site.xml
    <configuration>
      <property>
        <name>fs.default.name</name>
        <value>hdfs://hadoop000:8020</value>
      </property>
    </configuration>
    Esc 右下角bot模式  :wq!

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
    Esc 右下角bot模式  :wq!

    cp mapred-site.xml.tempate mapred-site.xml
    vi mapred-site.xml
    <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
    </property>
    Esc 右下角bot模式  :wq!

    vi yarn-site.xml
    <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
    </property>
    Esc 右下角bot模式  :wq!

    cd ~/app/hadoop-2.6.0-cdh5.7.0/bin
    查看 /app/tmp 目录是空的
    ./hadoop namenode -format 
    Y
    查看信息 Storage directory /home/hadoop/app/tmp/dfs/name has been successfully formatted.

    修改hosts
    sudo vi /etc/hosts
    127.0.0.1 localhost
    127.0.0.1
    localhost
    127.0.0.1 hadoop000

    Esc 右下角bot模式  :wq!



    cd ~/app/hadoop-2.6.0-cdh5.7.0/sbin    
    ./start-dfs.sh
    jps

    显示：
    jps
    NameNode
    DataNode
    SecondaryNode

    hadoop fs -ls /

    ./start-yarn.sh
    http://192.168.10.92:50070
    http://192.168.10.92:8088
  ```


  maven环境搭建  
  ```shell    
    tar -zxvf apache-maven-3.3.9 -C ~/app/
    vi ~/.bash_profile
    export MAVEN_HOME=/home/hadoop/app/apache-maven-3.3.9
    export PATH=$MAVEN_HOME/bin:$PATH
    Esc 右下角bot模式  :wq!
    source ~/.bash_profile
    
    注意setting.xml  修改仓库地址 localRepository


  ```


  python环境搭建   
  ```shell    
    tar -zxvf Python-3.6.5.tgz -C ~/app/software
    cd Python-3.6.5
    sudo vi /usr/bin/yum 
    修改 第一行 python  改为 python2.6
    yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel splite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
    ./configure --prefix=/home/hadoop/app/python3
  ```

  Spark环境搭建   
  ```shell    
    cd /home/hadoop/source/spark-2.3.0/dev
    编译spark
    ./dev/make-distribution.sh --name custom-spark --pip --r --tgz -Psparkr -Phadoop-2.7 -Phive -Phive-thriftserver -Pmesos -Pyarn -Pkubernetes

    make-distribution.sh --name 2.6.0-cdh5.7.0 --tgz -Pyarn -Phadoop-2.6 -Phive -Phive-thriftserver -Dhadoop.version=2.6.0-cdh5.7.0

    解压到 app/
    cd /home/hadoop/app/spark-2.3.0-bin-2.6.0-cdh5.7.0/bin
    ./spark-shell

    http://hadoop000:4040



  ```
  
  最简单做法：修改虚拟机host；启动 hadoop 和 spark

## 第3章 Spark Core核心RDD 
 https://github.com/apache/spark
Resilient Distributed Dataset (RDD)  弹性 分布式 数据集

Represents an immutable, partitioned collection of elements that can be operated on in parallel
不可变 并行操作

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


