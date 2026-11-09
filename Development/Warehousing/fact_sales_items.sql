-- Databricks notebook source
CREATE OR REPLACE TABLE retail_crm_dw.dw.fact_sales_items AS

SELECT

    si.item_id,
    si.sale_id,

    s.customer_id,

    si.product_id,

    dc.channel_key,

    dca.campaign_key,

    dd.date_key,

    si.quantity,

    si.original_price,

    si.unit_price,

    si.discount_applied,

    si.discount_percent,

    si.discounted,

    si.item_total

FROM retail_crm_dw.stg.stg_sales_items si

INNER JOIN retail_crm_dw.stg.stg_sales s
    ON si.sale_id = s.sale_id

LEFT JOIN retail_crm_dw.dw.dim_channel dc
    ON si.channel = dc.channel

LEFT JOIN retail_crm_dw.dw.dim_date dd
    ON si.sale_date = dd.full_date

LEFT JOIN retail_crm_dw.dw.dim_campaign dca
    ON si.channel_campaigns = dca.channel
   AND si.sale_date BETWEEN dca.start_date AND dca.end_date;