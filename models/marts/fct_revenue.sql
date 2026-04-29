-- fct_revenue: daily aggregated revenue metrics
-- grain: one row per order_date

select
    order_date,
    sum(amount) as total_revenue,
    count(order_id) as total_orders,
    count(distinct customer_id) as unique_customers
from {{ ref('stg_orders') }}
group by order_date
order by order_date