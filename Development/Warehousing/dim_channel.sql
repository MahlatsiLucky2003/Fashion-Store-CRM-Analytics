-- Databricks notebook source
CREATE OR REPLACE TABLE retail_crm_dw.dw.dim_channel AS
SELECT
    ROW_NUMBER() OVER (ORDER BY channel) AS channel_key,
    channel,
    description
FROM retail_crm_dw.stg.stg_channels;