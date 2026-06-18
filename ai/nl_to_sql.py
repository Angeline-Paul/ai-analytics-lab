from google.cloud import bigquery


PROJECT_ID = "ai-analytics-lab"
DATASET = "dbt_dev"


def generate_sql(question: str) -> str:
    """
    Convert a business question into an approved SQL query.
    This is a controlled rule-based prototype.
    """

    question = question.lower()

    if "high value" in question:
        return f"""
select *
from `{PROJECT_ID}.{DATASET}.customer_segments`
where customer_segment = 'High Value'
"""

    if "highest revenue" in question or "lifetime value" in question:
        return f"""
select
    customer_id,
    lifetime_value
from `{PROJECT_ID}.{DATASET}.fct_customer_kpis`
order by lifetime_value desc
"""

    if "daily revenue" in question or "revenue trend" in question:
        return f"""
select *
from `{PROJECT_ID}.{DATASET}.fct_revenue`
order by order_date
"""

    return ""


def run_query(sql: str):
    """
    Execute generated SQL in BigQuery and return results.
    """

    client = bigquery.Client(project=PROJECT_ID)
    query_job = client.query(sql)
    return query_job.result()


if __name__ == "__main__":
    question = input("Ask a business question: ")
    sql = generate_sql(question)

    if not sql:
        print("\nNo matching semantic query found.")
    else:
        print("\nGenerated SQL:")
        print(sql)

        print("\nBigQuery Results:")
        results = run_query(sql)

        for row in results:
            print(dict(row))