-- Databricks notebook source
CREATE OR REPLACE TABLE retail_crm_dw.dw.dim_customer AS
SELECT
    ROW_NUMBER() OVER (ORDER BY customer_id) AS customer_key,
    customer_id,
    country,
    age_range,
    signup_date
FROM retail_crm_dw.stg.stg_customers;