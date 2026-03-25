from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SilverLayer").getOrCreate()

df = spark.read.parquet("bronze/sales")

df_clean = df.dropna(subset=["amount"])
df_clean = df_clean.withColumn("amount", col("amount").cast("double"))

df_clean.write.mode("overwrite").parquet("silver/sales")

print("Silver layer completed")
