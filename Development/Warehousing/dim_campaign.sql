-- Databricks notebook source
CREATE OR REPLACE TABLE retail_crm_dw.dw.dim_campaign AS
SELECT
    ROW_NUMBER() OVER (ORDER BY campaign_id) AS campaign_key,
    campaign_id,
    campaign_name,
    channel,
    discount_type,
    discount_value,
    start_date,
    end_date
FROM retail_crm_dw.stg.stg_campaigns;