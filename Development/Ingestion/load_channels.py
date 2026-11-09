# Databricks notebook source
# Read CSV

channels_df = (
    spark.read
         .format("csv")
         .option("header", "true")
         .option("inferSchema", "true")
         .load("/Volumes/retail_crm_dw/stg/raw_files/dataset_fashion_store_channels.csv")
)

# Write Delta Table

(
    channels_df.write
               .format("delta")
               .mode("overwrite")
               .saveAsTable("retail_crm_dw.stg.stg_channels")
)

print("stg_channels loaded successfully")