from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spar_demo")\
    .config('spark.mongodb.input.uri','mongodb://192.168.1.96:27017/mydatabase.fdata')\
    .config('spark.mongodb.output.uri','mongodb://192.168.1.96:27017/mydatabase.fdata').getOrCreate()

#code for write
# abc = spark.read.csv('/home/tibil/Chetan/Tasks/Fire_Department_Calls.csv', header=True)
# abc.write.format('com.mongodb.spark.sql.DefaultSource').option('database','mydatabase').option('collection','fdata').save()



#code for read

df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.1.96:27017/mydatabase.fdata").load()

print(df.show())
