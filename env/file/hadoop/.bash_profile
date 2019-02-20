
export JAVA_HOME=/home/hadoop/app/jdk1.8.0_91
export PATH=$JAVA_HOME/bin:$PATH

export SCALA_HOME=/home/hadoop/app/scala-2.11.8
export PATH=$SCALA_HOME/bin:$PATH


export HADOOP_HOME=/home/hadoop/app/hadoop-2.6.0-cdh5.7.0
export PATH=$HADOOP_HOME/bin:$PATH

export MAVEN_HOME=/home/hadoop/app/apache-maven-3.3.9
export PATH=$MAVEN_HOME/bin:$PATH

export PATH=/home/hadoop/app/python3/bin:/usr/bin/python:$PATH
export PYSPARK_PYTHON=python

export SPARK_HOME=/home/hadoop/app/spark-2.3.0-bin-2.6.0-cdh5.7.0
export PATH=$SPARK_HOME/bin:$PATH

export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native

export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"

