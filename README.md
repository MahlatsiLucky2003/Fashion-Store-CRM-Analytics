# Fashion Store CRM Analytics

## Project Overview

Fashion Store CRM Analytics is an end-to-end analytics solution developed using Databricks and Power BI.

The project is based on a simulated European fashion retail company operating through E-commerce and Mobile App channels. The dataset is entirely fictional and was created for educational and portfolio purposes while reflecting realistic retail business scenarios and analytics challenges.

The solution transforms raw transactional data into actionable business insights through data ingestion, warehousing, orchestration, semantic modelling, and interactive reporting.

Business users can analyse customer behaviour, product performance, campaign effectiveness, channel contribution, and overall sales performance through a centralised analytics platform.

---

## Dataset Disclaimer

This project uses a simulated retail dataset representing a fictional European fashion retailer. All customers, products, transactions, campaigns, and business operations contained within the dataset are fictitious and intended solely for educational, analytical, and portfolio purposes.

---

## Problem Statement

Fashion retailers generate large volumes of transactional data across multiple digital channels. Although valuable insights exist within this data, raw datasets alone do not support effective decision-making.

Business stakeholders require a centralised analytics solution capable of answering key questions such as:

- Which products generate the most revenue?
- Which customer segments contribute the highest sales?
- Which marketing campaigns are the most effective?
- How do sales channels compare in performance?
- What are the overall sales and profitability trends?

Without a structured analytics platform, answering these questions becomes difficult, time-consuming, and inefficient.

---

## Objectives

- Build an end-to-end analytics solution using Databricks and Power BI.
- Design and implement a dimensional data warehouse using a Star Schema.
- Automate data ingestion and transformation processes.
- Develop a semantic model to support business reporting.
- Create interactive dashboards for business users and decision-makers.
- Deliver actionable insights across sales, customers, products, campaigns, and channels.

---

## KPI Metrics

### Sales Metrics

- Total Sales
- Total Orders
- Average Order Value (AOV)
- Gross Profit
- Profit Margin %

### Customer Metrics

- Total Customers

### Product Metrics

- Total Quantity Sold
- Products Sold

### Campaign Metrics

- Discounted Orders
- Total Discount Amount

---

## Solution Overview

The solution follows a modern analytics architecture where raw CSV files are ingested into Databricks, transformed into Delta Lake tables, modelled within a dimensional data warehouse, orchestrated through Databricks Jobs, and ultimately consumed in Power BI.

The final solution provides stakeholders with interactive reports and dashboards that support data-driven decision-making across sales, products, customers, channels, and campaigns.

---

## Architecture Diagram

### Solution Architecture

> Replace the placeholder below with your architecture diagram screenshot.

![Architecture Diagram](images/architecture-diagram.png)

---

# Dashboard Pages

## Sheet 1: Executive Overview

### Overview

The Executive Overview dashboard provides leadership with a comprehensive summary of overall business performance. It focuses on revenue, profitability, orders, customer activity, and sales trends to support strategic decision-making.

### KPI Cards

- Total Sales
- Total Orders
- Total Customers
- Average Order Value
- Gross Profit

### Visualisations

- Monthly Sales Trend
- Revenue by Country
- Revenue by Channel
- Orders by Month

### Filters

- Date
- Country

### Dashboard Screenshot

![Executive Overview](images/sheet1-executive-overview.png)

---

## Sheet 2: Product Performance

### Overview

The Product Performance dashboard evaluates product, category, and brand performance to help identify top-performing products and profitable categories.

### KPI Cards

- Total Sales
- Products Sold
- Total Quantity Sold
- Gross Profit
- Profit Margin %

### Visualisations

- Revenue by Category
- Revenue by Brand
- Top 10 Products by Revenue
- Profit by Category

### Filters

- Date
- Category

### Dashboard Screenshot

![Product Performance](images/sheet2-product-performance.png)

---

## Sheet 3: Customer Analytics

### Overview

The Customer Analytics dashboard provides insights into customer demographics and purchasing behaviour, helping identify valuable customer segments and market opportunities.

### KPI Cards

- Total Customers
- Total Orders
- Total Sales
- Average Order Value
- Total Quantity Sold

### Visualisations

- Revenue by Age Range
- Customers by Country
- Orders by Age Range
- Customer Registration Trend

### Filters

- Date
- Age Range

### Dashboard Screenshot

![Customer Analytics](images/sheet3-customer-analytics.png)

---

## Sheet 4: Campaign Performance

### Overview

The Campaign Performance dashboard measures the effectiveness of marketing campaigns and assesses how promotional activities influence customer purchasing behaviour and revenue generation.

### KPI Cards

- Total Sales
- Total Orders
- Discounted Orders
- Total Discount Amount
- Average Order Value

### Visualisations

- Revenue by Campaign
- Discount Amount by Campaign
- Orders by Campaign
- Campaign Revenue Trend

### Filters

- Date
- Campaign Name

### Dashboard Screenshot

![Campaign Performance](images/sheet4-campaign-performance.png)

---

## Sheet 5: Channel Performance

### Overview

The Channel Performance dashboard analyses sales contributions across channels and compares customer engagement and revenue generation between E-commerce and Mobile App platforms.

### KPI Cards

- Total Sales
- Total Orders
- Total Customers
- Average Order Value
- Profit Margin %

### Visualisations

- Revenue by Channel
- Orders by Channel
- Customers by Channel
- Monthly Sales by Channel

### Filters

- Date
- Channel

### Dashboard Screenshot

![Channel Performance](images/sheet5-channel-performance.png)

---

# Tasks Performed

## Data Ingestion

- Created PySpark ingestion notebooks.
- Loaded raw CSV files into Delta Lake tables.
- Performed data validation and quality checks.
- Standardised and cleansed source data.
- Converted percentage fields into numeric formats for analysis.

## Data Warehousing

- Designed a dimensional data warehouse.
- Implemented a Star Schema data model.
- Created staging and warehouse layers.
- Developed fact and dimension tables.
- Established business relationships between datasets.

## Workflow Orchestration

- Built Databricks Jobs for workflow automation.
- Configured task dependencies.
- Automated data loading and transformation processes.
- Implemented end-to-end ETL execution flow.

## Semantic Modelling

- Developed a Power BI semantic model.
- Created relationships between fact and dimension tables.
- Implemented KPI measures using DAX.
- Optimised the model for analytical reporting.

## Dashboard Development

- Developed five interactive dashboard pages.
- Built executive KPI scorecards.
- Created analytical visualisations and filters.
- Delivered business-focused reporting solutions.

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Data Platform | Databricks Free Edition |
| Data Processing | PySpark |
| Data Storage | Delta Lake |
| Data Warehouse | Star Schema |
| Query Language | SQL |
| Workflow Orchestration | Databricks Jobs |
| Business Intelligence | Microsoft Power BI |
| Semantic Modelling | Power BI Datafact_sales_items
