# Databricks notebook source
# Read CSV

customers_df = (
    spark.read
         .format("csv")
         .option("header", "true")
         .option("inferSchema", "true")
         .load("/Volumes/retail_crm_dw/stg/raw_files/dataset_fashion_store_customers.csv")
)

# Write Delta Table

(
    customers_df.write
                .format("delta")
                .mode("overwrite")
                .saveAsTable("retail_crm_dw.stg.stg_customers")
)

print("stg_customers loaded successfully")