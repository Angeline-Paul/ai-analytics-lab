-- dim_customers: master customer dimension
-- grain: one row per customer_id

select
    customer_id,
    customer_name,
    city,
    country
from {{ ref('customers') }}