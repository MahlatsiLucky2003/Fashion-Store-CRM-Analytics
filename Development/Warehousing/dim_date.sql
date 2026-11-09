-- Databricks notebook source
CREATE OR REPLACE TABLE retail_crm_dw.dw.dim_date AS
SELECT DISTINCT
    CAST(date_format(sale_date,'yyyyMMdd') AS INT) AS date_key,
    sale_date AS full_date,
    day(sale_date) AS day,
    month(sale_date) AS month,
    date_format(sale_date,'MMMM') AS month_name,
    quarter(sale_date) AS quarter,
    year(sale_date) AS year,
    date_format(sale_date,'EEEE') AS weekday
FROM retail_crm_dw.stg.stg_sales;