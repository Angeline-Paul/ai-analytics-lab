# Analytics Platform Runbook

## Pipeline Failure

### Step 1

Review dbt logs

```bash
dbt debug
```

### Step 2

Run failing model

```bash
dbt run --select model_name
```

### Step 3

Run validation tests

```bash
dbt test
```

### Step 4

Review BigQuery job history

### Step 5

Escalate to Analytics Engineering Team

---

## Documentation Failure

Run:

```bash
dbt docs generate
```

again.