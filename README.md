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
customers.csv (master/reference seed)
orders.csv (transactional seed)
          ↓ dbt seed
BigQuery: customers (raw master data)
BigQuery: orders (raw transactional data)

          ↓ dbt run

BigQuery: dim_customers (master dimension)
BigQuery: stg_orders (staging layer)

          ↓ dbt run

BigQuery: fct_revenue (fact/metrics layer)
BigQuery: dim_customer_metrics (derived dimension layer)
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

### 5. Master Dimension Layer

**`dim_customers`**

* Grain: one row per `customer_id`
* Master customer reference data

Columns:

* customer_id
* customer_name
* city
* country

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

## 📈 Current State (Day 5)

✔ dbt project structured into raw, staging, and marts layers  
✔ Connected to BigQuery with end-to-end pipeline execution  

✔ Seed-based source datasets implemented  
   - `orders` (transactional data)  
   - `customers` (master/reference data)  

✔ Staging layer implemented  
   - `stg_orders` standardizes transactional order data  

✔ Fact layer implemented  
   - `fct_revenue` provides daily aggregated business metrics  

✔ Dimension layers implemented  
   - `dim_customers` → master customer dimension  
   - `dim_customer_metrics` → derived behavioral customer metrics  

✔ Data quality and governance tests implemented  
   - `not_null` tests  
   - `unique` tests  
   - `relationships` tests (referential integrity)  

✔ Introduced dimensional modeling concepts  
   - separation of fact and dimension layers  
   - distinction between master and derived dimensions  
   - model grain definition and governance thinking  

✔ Project version-controlled and maintained on GitHub  
✔ README documentation continuously refined with modeling explanations  

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
