# Day 5 — Daily Log

## AI Analytics Lab

**Date:** 30 April 2026

---

# 🎯 Objective

Extend the analytics engineering project from basic transformations into a more realistic dimensional modeling structure by introducing:

* master customer dimension
* relationship testing
* referential integrity concepts
* warehouse-style architecture

---

# ✅ Work Completed

## 1. Added Master Customer Seed Data

Created:

```text
seeds/customers.csv
```

Purpose:

* simulate customer master/reference data
* separate transactional vs master entities

Columns:

* customer_id
* customer_name
* city
* country

---

## 2. Loaded Seed Data into BigQuery

Executed:

```bash
dbt seed
```

Result:

* `customers` table created in BigQuery
* source data successfully loaded into warehouse

---

## 3. Created True Customer Dimension

Created model:

```text
models/marts/dim_customers.sql
```

Purpose:

* establish proper master dimension structure
* separate customer attributes from transactional metrics

Implemented:

* customer_id
* customer_name
* city
* country

Concept introduced:

* master dimension modeling

---

## 4. Clarified Derived vs Master Dimensions

Refactored previous dimension naming:

```text
dim_customers
→
dim_customer_metrics
```

Reason:

* existing model represented behavioral metrics
* not true customer master data

Concept introduced:

* derived analytical dimension vs master dimension

---

## 5. Implemented Relationship Testing

Created relationship validation between:

```text
stg_orders.customer_id
→
dim_customers.customer_id
```

Purpose:

* enforce referential integrity
* validate that every order belongs to a valid customer

Implemented using YAML-based dbt tests.

---

## 6. Modernized dbt Test Syntax

Updated relationship test syntax to latest dbt-compatible format:

```yaml
arguments:
```

Purpose:

* remove deprecation warnings
* align with dbt 1.11 standards

---

## 7. Improved Project Architecture

Refined warehouse layering structure:

```text
Raw Layer
- orders
- customers

Staging Layer
- stg_orders

Dimension Layer
- dim_customers
- dim_customer_metrics

Fact Layer
- fct_revenue
```

Concepts introduced:

* dimensional modeling
* warehouse layering
* governance-oriented architecture

---

## 8. README Improvements

Enhanced documentation with:

* architecture updates
* grain definitions
* layer classifications
* dimensional modeling explanations
* current project state narrative

---

# 🧠 Key Learnings

* Difference between master and derived dimensions
* Importance of grain in dimensional modeling
* Relationship testing and referential integrity concepts
* YAML syntax structure and indentation handling
* dbt test modernization and deprecation handling
* Warehouse-oriented project organization

---

# ⚠️ Issues Encountered

## YAML Parsing Error

Issue:

* incorrect indentation in relationship tests

Resolution:

* corrected YAML spacing structure
* aligned test hierarchy properly

---

## GitHub Push Protection Error

Issue:

* GitHub blocked push due to exposed token

Resolution:

* removed tracked secret
* learned secure credential handling
* configured Git credential manager

Concept learned:

* secret management and repository security

---

# ✅ Final Status

Successfully completed:

```bash
dbt seed
dbt run
dbt test
```

Results:

* PASS=6
* WARN=0
* ERROR=0

---

# 🚀 Next Focus (Day 6)

Planned enhancements:

* optimize materialization strategy
* introduce star schema refinement
* improve marts architecture
* implement advanced KPIs
* strengthen analytics engineering design patterns



Day 5 log : 30-Apr-2026

Angeline@Angeline MINGW64 ~
$ cd /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ dbt seed
20:57:30  Running with dbt=1.11.8
20:57:35  Registered adapter: bigquery=1.11.1
20:57:36  Found 3 models, 2 seeds, 3 data tests, 539 macros
20:57:36
20:57:36  Concurrency: 1 threads (target='dev')
20:57:36
20:57:39  1 of 2 START seed file dbt_dev.customers ....................................... [RUN]
20:57:46  1 of 2 OK loaded seed file dbt_dev.customers ................................... [INSERT 4 in 6.71s]
20:57:46  2 of 2 START seed file dbt_dev.orders .......................................... [RUN]
20:57:53  2 of 2 OK loaded seed file dbt_dev.orders ...................................... [INSERT 5 in 7.07s]
20:57:53
20:57:53  Finished running 2 seeds in 0 hours 0 minutes and 16.59 seconds (16.59s).
20:57:53
20:57:53  Completed successfully
20:57:53
20:57:53  Done. PASS=2 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=2

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ dbt run
21:00:43  Running with dbt=1.11.8
21:00:44  Registered adapter: bigquery=1.11.1
21:00:45  Found 4 models, 2 seeds, 3 data tests, 539 macros
21:00:45
21:00:45  Concurrency: 1 threads (target='dev')
21:00:45
21:00:48  1 of 4 START sql view model dbt_dev.dim_customers .............................. [RUN]
21:00:50  1 of 4 OK created sql view model dbt_dev.dim_customers ......................... [CREATE VIEW (0 processed) in 2.07s]
21:00:50  2 of 4 START sql view model dbt_dev.stg_orders ................................. [RUN]
21:00:52  2 of 4 OK created sql view model dbt_dev.stg_orders ............................ [CREATE VIEW (0 processed) in 2.06s]
21:00:52  3 of 4 START sql view model dbt_dev.dim_customer_metrics ....................... [RUN]
21:00:54  3 of 4 OK created sql view model dbt_dev.dim_customer_metrics .................. [CREATE VIEW (0 processed) in 2.07s]
21:00:54  4 of 4 START sql view model dbt_dev.fct_revenue ................................ [RUN]
21:00:56  4 of 4 OK created sql view model dbt_dev.fct_revenue ........................... [CREATE VIEW (0 processed) in 1.96s]
21:00:56
21:00:56  Finished running 4 view models in 0 hours 0 minutes and 10.81 seconds (10.81s).
21:00:56
21:00:56  Completed successfully
21:00:56
21:00:56  Done. PASS=4 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=4

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ dbt test
21:15:26  Running with dbt=1.11.8
21:15:28  Registered adapter: bigquery=1.11.1
21:15:29  [WARNING][MissingArgumentsPropertyInGenericTestDeprecation]: Deprecated
functionality
Found top-level arguments to test `relationships` defined on 'stg_orders' in
package 'ai_analytics_lab' (models\marts\schema.yml). Arguments to generic tests
should be nested under the `arguments` property.
21:15:29  Found 4 models, 2 seeds, 6 data tests, 539 macros
21:15:29
21:15:29  Concurrency: 1 threads (target='dev')
21:15:29
21:15:31  1 of 6 START test not_null_dim_customer_metrics_customer_id .................... [RUN]
21:15:34  1 of 6 PASS not_null_dim_customer_metrics_customer_id .......................... [PASS in 3.30s]
21:15:34  2 of 6 START test not_null_dim_customers_customer_id ........................... [RUN]
21:15:37  2 of 6 PASS not_null_dim_customers_customer_id ................................. [PASS in 2.77s]
21:15:37  3 of 6 START test not_null_fct_revenue_order_date .............................. [RUN]
21:15:39  3 of 6 PASS not_null_fct_revenue_order_date .................................... [PASS in 2.55s]
21:15:39  4 of 6 START test relationships_stg_orders_customer_id__customer_id__ref_dim_customers_  [RUN]
21:15:42  4 of 6 PASS relationships_stg_orders_customer_id__customer_id__ref_dim_customers_  [PASS in 2.52s]
21:15:42  5 of 6 START test unique_dim_customer_metrics_customer_id ...................... [RUN]
21:15:44  5 of 6 PASS unique_dim_customer_metrics_customer_id ............................ [PASS in 2.62s]
21:15:44  6 of 6 START test unique_dim_customers_customer_id ............................. [RUN]
21:15:47  6 of 6 PASS unique_dim_customers_customer_id ................................... [PASS in 2.78s]
21:15:47
21:15:47  Finished running 6 data tests in 0 hours 0 minutes and 18.10 seconds (18.10s).
21:15:47
21:15:47  Completed successfully
21:15:47
21:15:47  Done. PASS=6 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=6
21:15:47  [WARNING][DeprecationsSummary]: Deprecated functionality
Summary of encountered deprecations:
- MissingArgumentsPropertyInGenericTestDeprecation: 1 occurrence
To see all deprecation instances instead of just the first occurrence of each,
run command again with the `--show-all-deprecations` flag. You may also need to
run with `--no-partial-parse` as some deprecations are only encountered during
parsing.

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ ^C

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ dbt test
21:19:07  Running with dbt=1.11.8
21:19:08  Registered adapter: bigquery=1.11.1
21:19:09  Encountered an error:
Parsing Error
  Error reading ai_analytics_lab: marts\schema.yml - Runtime Error
    Syntax error near line 41
    ------------------------------
    38 |     columns:
    39 |       - name: customer_id
    40 |         tests:
    41 |        - relationships:
    42 |            arguments:
    43 |               to: ref('dim_customers')
    44 |               field: customer_id

    Raw Error:
    ------------------------------
    while scanning for the next token
    found character that cannot start any token
      in "<unicode string>", line 41, column 7

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ ^C

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ dbt test
21:21:39  Running with dbt=1.11.8
21:21:41  Registered adapter: bigquery=1.11.1
21:21:42  Encountered an error:
Parsing Error
  Error reading ai_analytics_lab: marts\schema.yml - Runtime Error
    Syntax error near line 42
    ------------------------------
    39 |       - name: customer_id
    40 |         tests:
    41 |           - relationships:
    42 |              arguments:
    43 |                 to: ref('dim_customers')
    44 |                 field: customer_id

    Raw Error:
    ------------------------------
    while scanning for the next token
    found character that cannot start any token
      in "<unicode string>", line 42, column 1

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ dbt test
21:22:30  Running with dbt=1.11.8
21:22:32  Registered adapter: bigquery=1.11.1
21:22:34  Found 4 models, 2 seeds, 6 data tests, 539 macros
21:22:34
21:22:34  Concurrency: 1 threads (target='dev')
21:22:34
21:22:36  1 of 6 START test not_null_dim_customer_metrics_customer_id .................... [RUN]
21:22:39  1 of 6 PASS not_null_dim_customer_metrics_customer_id .......................... [PASS in 3.00s]
21:22:39  2 of 6 START test not_null_dim_customers_customer_id ........................... [RUN]
21:22:41  2 of 6 PASS not_null_dim_customers_customer_id ................................. [PASS in 2.61s]
21:22:41  3 of 6 START test not_null_fct_revenue_order_date .............................. [RUN]
21:22:44  3 of 6 PASS not_null_fct_revenue_order_date .................................... [PASS in 2.42s]
21:22:44  4 of 6 START test relationships_stg_orders_customer_id__customer_id__ref_dim_customers_  [RUN]
21:22:46  4 of 6 PASS relationships_stg_orders_customer_id__customer_id__ref_dim_customers_  [PASS in 2.37s]
21:22:46  5 of 6 START test unique_dim_customer_metrics_customer_id ...................... [RUN]
21:22:49  5 of 6 PASS unique_dim_customer_metrics_customer_id ............................ [PASS in 2.41s]
21:22:49  6 of 6 START test unique_dim_customers_customer_id ............................. [RUN]
21:22:52  6 of 6 PASS unique_dim_customers_customer_id ................................... [PASS in 3.13s]
21:22:52
21:22:52  Finished running 6 data tests in 0 hours 0 minutes and 17.67 seconds (17.67s).
21:22:52
21:22:52  Completed successfully
21:22:52
21:22:52  Done. PASS=6 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=6

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ ^M

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ git add .
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ git commit -m "Update relationship tests to modern dbt syntax"
[main 395dd2f] Update relationship tests to modern dbt syntax
 4 files changed, 68 insertions(+), 11 deletions(-)
 create mode 100644 models/marts/dim_customers.sql
 create mode 100644 seeds/customers.csv

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ git push
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 4 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.62 KiB | 828.00 KiB/s, done.
Total 9 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/Angeline-Paul/ai-analytics-lab.git
   6c889f7..395dd2f  main -> main

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ git add .
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ git commit -m "Update relationship tests to modern dbt syntax"
[main adc0f7b] Update relationship tests to modern dbt syntax
 1 file changed, 14 insertions(+), 8 deletions(-)

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 514 bytes | 514.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Angeline-Paul/ai-analytics-lab.git
   395dd2f..adc0f7b  main -> main

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab (main)
$