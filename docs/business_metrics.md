# Business Metrics Dictionary

## total_revenue
Definition:
Total revenue generated from all customer orders.

Calculation:
SUM(amount)

Business Meaning:
Measures overall sales performance.

---

## total_orders
Definition:
Total number of customer orders.

Calculation:
COUNT(order_id)

Business Meaning:
Measures transaction volume.

---

## lifetime_value
Definition:
Total historical spend per customer.

Calculation:
SUM(amount) grouped by customer_id

Business Meaning:
Measures long-term customer value.

---

## avg_order_value
Definition:
Average spend per order.

Calculation:
AVG(amount)

Business Meaning:
Measures customer purchasing behavior.

---

## customer_segment
Definition:
Business categorization of customers based on lifetime spend.

Categories:
- High Value
- Medium Value
- Low Value

Business Meaning:
Supports customer targeting and segmentation analysis.