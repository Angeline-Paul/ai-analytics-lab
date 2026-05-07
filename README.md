# AI Analytics Lab

This repository documents a hands-on analytics engineering project built using dbt and BigQuery.
The goal is to demonstrate end-to-end data modeling, transformation, and validation using modern data stack tools.

---

## 🚀 Project Overview

This project implements a simple but structured ELT pipeline:

**Raw Data → Staging → Metrics (Fact Table) → Dimension (Derived Table) -> Data Quality Validation**

It simulates a transactional dataset and transforms it into business-ready analytics models.

---

## 🏗️ Analytics Engineering Architecture

```
CSV Seeds (Local Files)
        ↓
     dbt seed
        ↓
BigQuery Raw Layer
(orders, customers)
        ↓
     dbt run
        ↓
Staging Layer
(stg_orders)
        ↓
     dbt run
        ↓
Fact & KPI Layer
(fct_revenue, fct_customer_kpis)
        ↓
     dbt run
        ↓
Dimension Layer
(dim_customers, dim_customer_metrics)
        ↓
     dbt run
        ↓
Semantic Analytics Layer
(customer_segments)
        ↓
 dbt docs generate
        ↓
Metadata + Lineage Layer
(manifest.json, catalog.json, DAG)
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


### 2. Staging Layer

**`stg_orders`**

* Cleaned and standardized version of raw data
* Acts as the base for downstream models


### 3. Metrics Layer (Fact Table)

**`fct_revenue`**

* Grain: one row per `order_date`
* Aggregated business metrics

Metrics:

* total_revenue → sum(amount)
* total_orders → count(order_id)
* unique_customers → count(distinct customer_id)


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

---

## 🧪 Data Quality & Testing

Implemented using dbt YAML configuration:

* **not_null test** on `order_date` and `customer_id`
* Ensures critical fields are populated
* Validated using:

  ```
  dbt test
  ```
---

## 📚 Generated Analytics Documentation

The project uses dbt Docs to generate:
- interactive lineage DAGs
- metadata catalogs
- model documentation
- dependency visualization
- semantic analytics documentation

Generated artifacts:
- manifest.json
- catalog.json
- compiled SQL metadata

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

## 📈 Current State (Day 8)

✔ dbt project fully connected to BigQuery
✔ Seed-based raw ingestion layer implemented
✔ Staging transformations implemented using dbt models
✔ Fact tables created for revenue and customer KPIs
✔ Dimension tables implemented for customer analytics
✔ Customer segmentation semantic model created
✔ YAML-based testing and governance implemented
✔ dbt documentation site generated
✔ Lineage DAG successfully visualized
✔ Model metadata and documentation added
✔ Analytics engineering architecture established
✔ Semantic analytics structure introduced
✔ AI-ready analytics project organization implemented
✔ Project screenshots and architecture evidence captured
---

## 🧠 Key Learnings

* Understood how dbt generates machine-readable metadata artifacts
* Learned the role of manifest.json and catalog.json in analytics engineering
* Built lineage-aware analytics transformations using dbt refs
* Implemented semantic business modeling concepts
* Understood the importance of governed analytics metadata
* Generated interactive dbt documentation and lineage DAGs
* Learned how analytics engineering supports AI-assisted querying
* Structured project documentation using assets and docs folders
* Introduced portfolio-grade analytics architecture organization
* Learned how modern AI analytics systems leverage semantic metadata layers

---

## 🔮 Next Steps

* Introduce natural language analytics querying concepts
* Simulate AI-generated SQL workflows
* Build semantic query examples for business users
* Add conversational analytics architecture concepts
* Expand semantic metadata descriptions
* Introduce AI-assisted analytics engineering patterns
* Prepare project for production-style deployment concepts
* Introduce orchestration and CI/CD analytics workflows

---

## 📌 Notes

This project is part of a structured upskilling plan focused on:

* Analytics Engineering
* AI-augmented Data Analytics
* Cloud-based Data Pipelines
