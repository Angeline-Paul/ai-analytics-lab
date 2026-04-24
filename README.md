# AI Analytics Lab

This repository documents a hands-on analytics engineering project built using dbt and BigQuery.
The goal is to demonstrate end-to-end data modeling, transformation, and validation using modern data stack tools.

---

## 🚀 Project Overview

This project implements a simple but structured ELT pipeline:

**Raw Data → Staging → Metrics (Fact Table) → Data Quality Validation**

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

## 🧪 Data Quality & Testing

Implemented using dbt YAML configuration:

* **not_null test** on `order_date`
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

## 📈 Current State (Day 3)

✔ dbt project initialized
✔ Connected to BigQuery
✔ Seed data loaded
✔ Staging model created
✔ Metrics model (fct_revenue) implemented
✔ Data quality tests added

---

## 🧠 Key Learnings

* Implemented ELT workflow using dbt
* Understood separation of raw, staging, and metrics layers
* Built first fact table with business-level aggregation
* Introduced data validation using YAML-based tests
* Executed full pipeline in BigQuery

---

## 🔮 Next Steps

* Add dimension tables (e.g., dim_customers)
* Implement relationships between models
* Introduce advanced tests (unique, relationships)
* Improve model structure (star schema)
* Add AI-assisted querying layer

---

## 📌 Notes

This project is part of a structured upskilling plan focused on:

* Analytics Engineering
* AI-augmented Data Analytics
* Cloud-based Data Pipelines

---
