from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("GoldLayer").getOrCreate()

df = spark.read.parquet("silver/sales")

df_gold = df.groupBy("product").agg(sum("amount").alias("total_sales"))

df_gold.write.mode("overwrite").parquet("gold/sales_summary")

print("Gold layer completed")
