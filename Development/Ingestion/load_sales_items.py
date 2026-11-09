# Databricks notebook source
from pyspark.sql.functions import regexp_replace, col

# Read CSV

sales_items_df = (
    spark.read
         .format("csv")
         .option("header", "true")
         .option("inferSchema", "true")
         .load("/Volumes/retail_crm_dw/stg/raw_files/dataset_fashion_store_salesitems.csv")
)

# Clean discount_percent

sales_items_df = sales_items_df.withColumn(
    "discount_percent",
    regexp_replace(col("discount_percent"), "%", "")
        .cast("decimal(10,2)")
)

# Write Delta Table

(
    sales_items_df.write
                  .format("delta")
                  .mode("overwrite")
                  .saveAsTable("retail_crm_dw.stg.stg_sales_items")
)

print("stg_sales_items loaded successfully")