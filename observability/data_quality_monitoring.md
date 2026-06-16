# Data Quality Monitoring

## Orders Validation

Critical Checks:

* order_id not null
* customer_id not null
* amount > 0

---

## Customer Validation

Critical Checks:

* customer_id unique
* customer_name populated

---

## KPI Validation

Revenue Validation:

* total_revenue must reconcile to source transactions

Customer KPI Validation:

* customer counts must reconcile to customer master records

---

## Monitoring Frequency

Daily
