def generate_sql(question: str) -> str:
    """
    Convert a business question into an approved SQL query.

    This is a controlled rule-based prototype.
    Later, this logic can be replaced or enhanced with an LLM.
    """

    question = question.lower()

    if "high value" in question:
        return """
select *
from `dbt_dev.customer_segments`
where customer_segment = 'High Value'
"""

    if "highest revenue" in question or "lifetime value" in question:
        return """
select
    customer_id,
    lifetime_value
from `dbt_dev.fct_customer_kpis`
order by lifetime_value desc
"""

    if "daily revenue" in question or "revenue trend" in question:
        return """
select *
from `dbt_dev.fct_revenue`
order by order_date
"""

    return "No matching semantic query found."


if __name__ == "__main__":
    question = input("Ask a business question: ")
    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)