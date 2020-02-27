from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark_json")\
     .config("spark.mongodb.input.uri","mongodb://192.168.1.96:27017/test.abc") \
    .config("spark.mongodb.output.uri","mongodb://192.168.1.96:27017/test.abc").getOrCreate()

# code for write json file data into mongodb

abc =spark.read.json("/home/tibil/Downloads/restaurants.json")

abc.write.format("com.mongodb.spark.sql.DefaultSource").option("database","test").option("collection","abc").save()




#code is for read data from mongoDB
#
# df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.1.96:27017/test.abc").load()
#
# print(df.show())
