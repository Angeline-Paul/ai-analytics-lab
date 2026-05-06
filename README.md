# AI Analytics Lab

This repository documents a hands-on analytics engineering project built using dbt and BigQuery.
The goal is to demonstrate end-to-end data modeling, transformation, and validation using modern data stack tools.

---

## 🚀 Project Overview

This project implements a simple but structured ELT pipeline:

**Raw Data → Staging → Metrics (Fact Table) → Dimension (Derived Table) -> Data Quality Validation**

It simulates a transactional dataset and transforms it into business-ready analytics models.

---

## 🏗️ Architecture

```
customers.csv
orders.csv

        ↓ dbt seed

BigQuery Raw Layer
- customers
- orders

        ↓ dbt run

BigQuery Staging Layer
- stg_orders (VIEW)

        ↓ dbt run

BigQuery Dimension Layer
- dim_customers (TABLE)
- dim_customer_metrics (TABLE)

BigQuery Fact Layer
- fct_revenue (TABLE)
- fct_customer_kpis (TABLE)

        ↓ dbt run

BigQuery Semantic Analytics Layer
- customer_segments (TABLE)
```
---

## ⚙️ Tools & Technologies

* dbt (Core) — transformation & modeling
* BigQuery — cloud data warehouse
* SQL — data transformations
* GitHub — version control

---

## 📊 Data Model

### 1. Raw Layer

**`orders`**

* Source: CSV seed file
* Contains transactional order data

Columns:

* order_id
* customer_id
* order_date
* amount

---

### 2. Staging Layer

**`stg_orders`**

* Cleaned and standardized version of raw data
* Acts as the base for downstream models

---

### 3. Metrics Layer (Fact Table)

**`fct_revenue`**

* Grain: one row per `order_date`
* Aggregated business metrics

Metrics:

* total_revenue → sum(amount)
* total_orders → count(order_id)
* unique_customers → count(distinct customer_id)

---

### 4. Dimension Layer (Derived)

**`dim_customer_metrics`**

* Grain: one row per `customer_id`
* Derived from transactional data (not master data)
* Represents customer behavior, not attributes

Metrics:

* total_orders → count(order_id)
* total_spent → sum(amount)
* first_order_date → min(order_date)
* last_order_date → max(order_date)

### 5. Master Dimension Layer

**`dim_customers`**

* Grain: one row per `customer_id`
* Master customer reference data

Columns:

* customer_id
* customer_name
* city
* country

### 6. Semantic Analytics Layer

**`customer_segments`**

* Grain: one row per `customer_id`
* Customer categorization model based on spending behavior

Logic:

* High Value → lifetime_value >= 500
* Medium Value → lifetime_value >= 200
* Low Value → lifetime_value < 200

## 🧪 Data Quality & Testing

Implemented using dbt YAML configuration:

* **not_null test** on `order_date` and `customer_id`
* Ensures critical fields are populated
* Validated using:

  ```
  dbt test
  ```
---

## 📊 dbt Lineage Graph

![Lineage](assets/full_project_dag.png)

---

## 🧠 Model Documentation

![Model Docs](assets/model_documentation.png)

---

## 🤖 AI-Augmented Analytics Engineering Features

This project incorporates AI-ready analytics engineering concepts:

- Semantic business metric definitions
- YAML-based metadata documentation
- Automated lineage generation using dbt docs
- Standardized KPI modeling
- Analytics-ready dimensional architecture
- Business-context-aware semantic models

The project is structured to support future AI-assisted querying and semantic analytics workflows.

---

## 🔄 How to Run This Project

### 1. Install dependencies

```
pip install dbt-core dbt-bigquery
```

### 2. Configure dbt profile

Set up `profiles.yml` with BigQuery credentials

### 3. Load data

```
dbt seed
```

### 4. Run models

```
dbt run
```

### 5. Run tests

```
dbt test
```

---

## 📈 Current State (Day 7)

✔ Cloud-native analytics engineering project implemented using dbt and BigQuery  

✔ Layered warehouse architecture established  
   - Raw Layer  
   - Staging Layer  
   - Dimension Layer  
   - Fact Layer  
   - Semantic Analytics Layer  

✔ Seed-based source ingestion implemented  
   - `orders.csv` → transactional source data  
   - `customers.csv` → master/reference source data  

✔ Staging layer implemented  
   - `stg_orders` standardizes and prepares transactional data for downstream modeling  

✔ Dimension models implemented  
   - `dim_customers` → master customer dimension  
   - `dim_customer_metrics` → derived behavioral customer metrics  

✔ Fact models implemented  
   - `fct_revenue` → daily aggregated revenue metrics  
   - `fct_customer_kpis` → customer-level KPI aggregation model  

✔ Semantic analytics layer implemented  
   - `customer_segments` categorizes customers into business segments  
   - segmentation based on customer lifetime value logic  

✔ Materialization strategy introduced  
   - staging models materialized as `VIEW`
   - marts/facts/dimensions materialized as `TABLE`

✔ Data governance and testing implemented  
   - `not_null` tests  
   - `unique` tests  
   - `relationships` tests for referential integrity  

✔ Warehouse-oriented modeling concepts introduced  
   - dimensional modeling  
   - fact vs dimension separation  
   - master vs derived dimensions  
   - semantic analytics modeling  
   - KPI engineering  

✔ Project fully version-controlled and maintained on GitHub  
✔ README continuously refined with architecture and modeling documentation

---

## 🧠 Key Learnings

* Implemented layered analytics engineering architecture using dbt and BigQuery
* Created the distinction between raw, staging, fact, dimension, and semantic analytics layers
* Built customer-centric KPI models using aggregation logic
* Introduced semantic business categorization through customer segmentation
* Refreshed dimensional modeling concepts including grain definition and relationship design
* Implemented warehouse optimization concepts using materialization strategies
* Applied data governance practices using YAML-based dbt tests
* Implemented referential integrity validation between transactional and master datasets
* Improved understanding of analytics engineering workflows and modern warehouse architecture
* Strengthened Git, GitHub, and repository management practices for portfolio development 

---

## 🔮 Next Steps

* Introduce AI-augmented analytics engineering concepts
* Implement semantic business metric documentation
* Generate automated lineage and metadata documentation using dbt docs
* Enhance YAML model descriptions for AI-readable analytics metadata
* Prepare project structure for natural language analytics workflows
* Add architecture visuals and lineage screenshots to GitHub README
* Introduce future AI analytics use-case planning and semantic querying concepts
* Strengthen project positioning as an AI-ready analytics engineering platform

---

## 📌 Notes

This project is part of a structured upskilling plan focused on:

* Analytics Engineering
* AI-augmented Data Analytics
* Cloud-based Data Pipelines

---
