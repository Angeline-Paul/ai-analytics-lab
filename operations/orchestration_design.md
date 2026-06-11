# Orchestration Design

## Future Orchestrator Options

### Apache Airflow

Pros:
- Industry standard
- Strong scheduling
- Enterprise adoption

### Microsoft Fabric Pipelines

Pros:
- Native Microsoft ecosystem
- Good Power BI integration

### dbt Cloud Jobs

Pros:
- Native dbt scheduling
- Easy deployment

---

## Recommended Architecture

```text
Scheduler
      ↓
dbt seed
      ↓
dbt run
      ↓
dbt test
      ↓
dbt docs generate
      ↓
Notification
```