# Databricks notebook source
from pyspark.sql.functions import regexp_replace, col

# Read CSV

campaigns_df = (
    spark.read
         .format("csv")
         .option("header", "true")
         .option("inferSchema", "true")
         .load("/Volumes/retail_crm_dw/stg/raw_files/dataset_fashion_store_campaigns.csv")
)

# Clean discount_value

campaigns_df = campaigns_df.withColumn(
    "discount_value",
    regexp_replace(col("discount_value"), "%", "")
        .cast("decimal(10,2)")
)

# Write Delta Table

(
    campaigns_df.write
                .format("delta")
                .mode("overwrite")
                .saveAsTable("retail_crm_dw.stg.stg_campaigns")
)

print("stg_campaigns loaded successfully")