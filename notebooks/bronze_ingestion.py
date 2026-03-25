from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BronzeLayer").getOrCreate()

df = spark.read.csv("data/sample_sales.csv", header=True, inferSchema=True)

df.write.mode("overwrite").parquet("bronze/sales")

print("Bronze layer completed")
