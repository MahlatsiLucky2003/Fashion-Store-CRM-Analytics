-- Databricks notebook source
CREATE OR REPLACE TABLE retail_crm_dw.dw.dim_product AS
SELECT
    ROW_NUMBER() OVER (ORDER BY product_id) AS product_key,
    product_id,
    product_name,
    category,
    brand,
    color,
    size,
    gender,
    catalog_price,
    cost_price
FROM retail_crm_dw.stg.stg_products;