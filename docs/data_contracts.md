# Data Contracts

## Orders Dataset

Owner:
Analytics Engineering Team

Expected Columns

| Column | Type |
|----------|----------|
| order_id | integer |
| customer_id | integer |
| order_date | date |
| amount | numeric |

SLA:
Daily refresh

Business Criticality:
High

---

## Customers Dataset

Owner:
Analytics Engineering Team

Expected Columns

| Column | Type |
|----------|----------|
| customer_id | integer |
| customer_name | string |
| city | string |
| country | string |

SLA:
Weekly refresh

Business Criticality:
Medium