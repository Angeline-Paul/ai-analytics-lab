-- dim_customer_metrics: customer-level behavioral metrics
-- grain: one row per customer_id
-- derived from transactional data (orders)

select
    customer_id,
    count(order_id) as total_orders,
    sum(amount) as total_spent,
    min(order_date) as first_order_date,
    max(order_date) as last_order_date
from {{ ref('stg_orders') }}
group by customer_id