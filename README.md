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
CSV (local seed)
   ↓ dbt seed
BigQuery: orders (raw layer)
   ↓ dbt run
BigQuery: stg_orders (staging layer)
   ↓ dbt run
BigQuery: fct_revenue (metrics layer)
   ↓ dbt run
BigQuery: dim_customer_metrics (Dimension layer)
```

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

## 4. Dimension Layer (Derived)

**`dim_customer_metrics`**

* Grain: one row per `customer_id`
* Derived from transactional data (not master data)
* Represents customer behavior, not attributes

Metrics:

* total_orders → count(order_id)
* total_spent → sum(amount)
* first_order_date → min(order_date)
* last_order_date → max(order_date)


## 🧪 Data Quality & Testing

Implemented using dbt YAML configuration:

* **not_null test** on `order_date` and `customer_id`
* Ensures critical fields are populated
* Validated using:

  ```
  dbt test
  ```

---

## ⚙️ Tools & Technologies

* dbt (Core) — transformation & modeling
* BigQuery — cloud data warehouse
* SQL — data transformations
* GitHub — version control

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

## 📈 Current State (Day 4)

✔ dbt project initialized and structured  
✔ Connected to BigQuery and running end-to-end  
✔ Seed data loaded and validated  

✔ Staging layer implemented (`stg_orders`)  
✔ Metrics layer implemented (`fct_revenue`)  
✔ Dimension layer added (`dim_customer_metrics`)  

✔ Data quality tests implemented (YAML-based)  
✔ Model documentation added (descriptions + grain clarity)  

✔ Basic dimensional modeling introduced  
   - separation of fact and dimension layers  
   - clear definition of grain for each model  

✔ Project version-controlled and maintained on GitHub  

---

## 🧠 Key Learnings

* Implemented end-to-end ELT workflow using dbt and BigQuery  
* Applied layered data modeling (raw → staging → marts)  
* Built fact table (`fct_revenue`) with defined grain and business metrics  
* Introduced dimension modeling with derived customer metrics (`dim_customer_metrics`)  
* Understood difference between transactional data, derived dimensions, and master data  
* Implemented data quality checks using YAML-based tests  
* Gained clarity on importance of grain in data modeling and its impact on relationships  

---

## 🔮 Next Steps

* Introduce true customer dimension (master data)  
* Establish relationships between fact and dimension tables  
* Implement advanced tests (unique, relationships, referential integrity)  
* Refactor models toward star schema design  
* Optimize materialization strategy (views vs tables)  
* Introduce AI-assisted querying and analytics layer 

---

## 📌 Notes

This project is part of a structured upskilling plan focused on:

* Analytics Engineering
* AI-augmented Data Analytics
* Cloud-based Data Pipelines

---
