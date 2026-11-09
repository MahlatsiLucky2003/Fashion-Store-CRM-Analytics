# Databricks notebook source
# Read CSV

sales_df = (
    spark.read
         .format("csv")
         .option("header", "true")
         .option("inferSchema", "true")
         .load("/Volumes/retail_crm_dw/stg/raw_files/dataset_fashion_store_sales.csv")
)

# Write Delta Table

(
    sales_df.write
            .format("delta")
            .mode("overwrite")
            .saveAsTable("retail_crm_dw.stg.stg_sales")
)

print("stg_sales loaded successfully")