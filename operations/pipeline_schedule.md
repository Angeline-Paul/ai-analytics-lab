# Pipeline Schedule

## Daily Analytics Pipeline

### 02:00

Load Source Data

### 02:15

dbt Seed

```bash
dbt seed
```

### 02:20

dbt Run

```bash
dbt run
```

### 02:30

dbt Test

```bash
dbt test
```

### 02:35

Generate Documentation

```bash
dbt docs generate
```

### 02:40

Publish Documentation

### 02:45

Notify Analytics Team

---

Pipeline Frequency:
Daily

Business SLA:
03:00 AM