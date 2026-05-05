-- customer_segments: customer segmentation model
-- grain: one row per customer_id

select
    customer_id,
    total_orders,
    lifetime_value,

    case
        when lifetime_value >= 500 then 'High Value'
        when lifetime_value >= 200 then 'Medium Value'
        else 'Low Value'
    end as customer_segment

from {{ ref('fct_customer_kpis') }}