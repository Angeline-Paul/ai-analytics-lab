# Metric to SQL Mapping

## Business Question

Which customers are High Value?

SQL

```sql
select *
from dbt_dev.customer_segments
where customer_segment = 'High Value'
```

---

## Business Question

Which customers generated the highest revenue?

SQL

```sql
select
    customer_id,
    lifetime_value
from dbt_dev.fct_customer_kpis
order by lifetime_value desc
```

---

## Business Question

How much revenue was generated each day?

SQL

```sql
select *
from dbt_dev.fct_revenue
order by order_date
```