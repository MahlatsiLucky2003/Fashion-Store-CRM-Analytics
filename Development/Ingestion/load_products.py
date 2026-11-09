# Databricks notebook source
# Read CSV

products_df = (
    spark.read
         .format("csv")
         .option("header", "true")
         .option("inferSchema", "true")
         .load("/Volumes/retail_crm_dw/stg/raw_files/dataset_fashion_store_products.csv")
)

# Write Delta Table

(
    products_df.write
              .format("delta")
              .mode("overwrite")
              .saveAsTable("retail_crm_dw.stg.stg_products")
)

print("stg_products loaded successfully")