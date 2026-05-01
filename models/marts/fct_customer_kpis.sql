-- fct_customer_kpis: customer-level business KPIs
-- grain: one row per customer_id

select
    customer_id,
    count(order_id) as total_orders,
    sum(amount) as lifetime_value,
    avg(amount) as avg_order_value,
    min(order_date) as first_order_date,
    max(order_date) as last_order_date
from {{ ref('stg_orders') }}
group by customer_id