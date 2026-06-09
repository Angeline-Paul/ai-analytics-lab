# AI Analytics Lab

Cloud-native Analytics Engineering and AI-Ready Analytics Platform built using dbt and BigQuery.

---

## 🎯 Business Problem

Organizations often struggle with:

- Inconsistent KPI definitions
- Siloed reporting logic
- Limited governance and lineage visibility
- Lack of semantic business definitions
- Challenges adopting AI-assisted analytics

This project demonstrates how modern analytics engineering practices can create a governed, semantic, and AI-ready analytics platform.

---

## ⚙️ Technology Stack

### Data Platform
- Google BigQuery

### Analytics Engineering
- dbt Core
- SQL
- YAML

### Version Control
- Git
- GitHub

### Documentation
- dbt Docs
- Markdown

### Analytics Concepts
- Dimensional Modeling
- Semantic Analytics
- Data Products
- Data Contracts
- AI-Ready Metadata

---


## 🤖 Natural Language Analytics Architecture

```
Business User
      ↓
Natural Language Question
      ↓
Semantic Analytics Layer
      ↓
Metric Definitions + Business Rules
      ↓
SQL Mapping
      ↓
BigQuery Models
      ↓
Business Insight
```
---

## 🏗️ Analytics Engineering Architecture

```
CSV Seeds
      ↓
dbt seed
      ↓
BigQuery Raw Layer
(customers, orders)
      ↓
dbt run
      ↓
Staging Layer
(stg_orders)
      ↓
dbt run
      ↓
Fact Layer
(fct_revenue)
(fct_customer_kpis)
      ↓
dbt run
      ↓
Dimension Layer
(dim_customers)
(dim_customer_metrics)
      ↓
dbt run
      ↓
Semantic Layer
(customer_segments)
      ↓
Business Questions
Metric Definitions
Metric-to-SQL Mapping
      ↓
AI Query Layer
(Future)
```
---

## 🤖 AI-Augmented Analytics Engineering Features

This project incorporates AI-ready analytics engineering concepts:

- Semantic business metric definitions
- YAML-based metadata documentation
- Automated lineage generation
- Standardized KPI modeling
- Analytics-ready dimensional architecture
- Business-context-aware semantic models

The project is structured to support future AI-assisted querying and semantic analytics workflows.

---

## 🏢 Enterprise Analytics Features

Beyond analytics engineering, this project incorporates enterprise data management concepts that support scalable and trustworthy analytics platforms.

### Governance

- Metric ownership
- Business definitions
- Data contracts
- Source documentation

### Analytics Products

- Customer KPI Product
- Revenue Analytics Product
- Customer Segmentation Product

### AI Readiness

- Semantic metric definitions
- Business question catalog
- Metric-to-SQL mappings
- AI-ready metadata architecture
- Lineage documentation

### Platform Capabilities

- dbt transformations
- BigQuery warehouse
- Data quality testing
- Documentation generation
- Semantic analytics layer

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


### 7. Semantic Documentation Layer

**`docs/semantic_layer/`**

* Contains business-readable analytics definitions
* Maps business questions to trusted dbt models
* Supports future natural-language-to-SQL workflows

Files:

* `business_questions.md` → catalog of business questions
* `metric_definitions.md` → governed metric definitions
* `metric_to_sql_mapping.md` → examples of business questions mapped to SQL

---

## 📚 Enterprise Documentation

### Data Contracts

```
docs/data_contracts.md
```

Defines:

- schema expectations
- ownership
- SLAs
- business criticality

---

### Data Products

```
docs/data_products.md
```

Defines:

- Customer KPI Product
- Revenue Analytics Product
- Customer Segmentation Product

---

### Governance

```
governance/metric_ownership.md
```

Defines:

- metric ownership
- accountability
- stewardship

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

## 🧠 Semantic Analytics Layer

This project includes a semantic analytics layer that bridges business language and warehouse queries.

The semantic layer includes:

* Business question catalog
* KPI and metric definitions
* Metric-to-SQL mappings
* AI-ready business context

This layer demonstrates how analytics systems can translate business questions into governed SQL queries using curated dbt models.

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

## 📈 Current State (Day 10)

* Cloud-native analytics engineering platform established
* Raw, staging, fact, dimension, and semantic layers implemented
* KPI engineering implemented
* Customer segmentation semantic model implemented
* dbt testing and governance implemented
* Lineage DAG generated
* Model metadata documented
* Business question catalog implemented
* Metric definitions documented
* Metric-to-SQL mappings created
* Data contracts introduced
* Data products defined
* Metric ownership documented
* Enterprise analytics architecture documented
* AI-ready semantic analytics foundation established

---

## 🧠 Key Learnings

- Built a modern analytics engineering workflow using dbt and BigQuery
- Implemented dimensional modeling and KPI engineering
- Learned semantic analytics concepts and business abstraction layers
- Understood how metadata supports AI-assisted analytics
- Introduced data contracts and governance concepts
- Implemented analytics product thinking
- Learned metric ownership and stewardship concepts
- Strengthened understanding of enterprise analytics architecture
- Built foundations required for future AI-assisted querying systems

---

## 🔮 Next Steps

The platform will continue evolving toward a production-grade, AI-enabled analytics architecture through the addition of:

- Production orchestration and scheduling
- Data observability and monitoring
- AI-assisted natural language querying
- Automated insight generation
- Data contracts and governance automation
- AI governance and trust frameworks
- Analytics agent prototypes
- Autonomous analytics workflows
- Retrieval-augmented analytics capabilities
- Enterprise deployment patterns

---

## 🔮 Future Roadmap

Planned enhancements include:

### Enterprise Analytics
- Production orchestration
- Data observability
- Data contracts
- Advanced governance

### AI-Augmented Analytics
- Natural language to SQL
- AI-generated business insights
- Semantic search across metrics
- Conversational analytics

### Autonomous Analytics
- KPI monitoring agents
- Anomaly detection
- Automated executive summaries
- Recommendation generation

### Platform Evolution
- Enterprise deployment architecture
- CI/CD integration
- AI governance controls
- Analytics product lifecycle management

---

## 📌 Notes

This project is part of a structured upskilling plan focused on:

* Analytics Engineering
* AI-augmented Data Analytics
* Cloud-based Data Pipelines
