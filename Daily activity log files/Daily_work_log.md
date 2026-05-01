## 22 April 2026

### What I did:
- checked python version
- installed dbt core and bigquery pluggin
- Checked dbt version
- installed latest version of pip
- Set up dbt project with bigquery as database
- Connected BigQuery 
	- created a colud project ai-analytics-lab
	- ran a sample query in query editor
	- created a dbt-service-account in IAM->service Accounts.
	- Generated a key and saved it in local folder
- Created dbt-project.yml with all the ai-analytics-lab project parameters
- CD to correct directory 
- debugged and ran the dbt project 
- Successfully ran first models

### Commands used:
- dbt init
- dbt debug
- dbt run

-----
$ python --version
Python 3.13.5

-----
$ pip install dbt-core dbt-bigquery

-----
$ dbt --version
Core:
  - installed: 1.11.8
  - latest:    1.11.8 - Up to date!

Plugins:
  - bigquery: 1.11.1 - Up to date!

---
$ python.exe -m pip install --upgrade pip

---
cd /c/Angeline/dbt_project/ai_analytics_lab

--
$ dbt init ai_analytics_lab

17:49:12  Setting up your profile.
Which database would you like to use?
[1] bigquery

select 1

---
Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab
$ cd ai_analytics_lab

Angeline@Angeline MINGW64 /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab
$ dbt debug


18:33:02  All checks passed!

---
$ dbt run
18:35:31  Completed successfully


--
### Issues:
- Path error fixed in dbt_project.yml location


---------------------------------------

# Daily Log — Day 2 (dbt + BigQuery Foundation)

## Date
23 April 2026

---

## Objective
Build and validate a basic ELT pipeline using dbt and BigQuery.

CSV (local)
   ↓ dbt seed
BigQuery: orders
   ↓ dbt run
BigQuery: stg_orders

---

## What I Worked On

### 1. Data Setup
- Created seed dataset (`orders.csv`)
- Defined simple transactional dataset with order-level data

### 2. dbt Execution
- Ran `dbt seed` to load raw data into BigQuery
- Verified data available in `orders` table

### 3. Transformation Layer
- Created staging model: `stg_orders.sql`
- Applied basic transformation using dbt ref()

### 4. Pipeline Execution
- Ran `dbt run`
- Successfully created staging model in BigQuery

---

Steps:

$ cd /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab
-----
$ cd models/example

delete this folder
------
Create a new orders.csv file inside seeds folder, with the following table structure:
order_id,customer_id,order_date,amount
1,101,2024-01-01,100
2,102,2024-01-02,200
3,101,2024-01-03,150
4,103,2024-01-04,300
5,104,2024-01-05,250

$ cd seeds/orders.csv
-----
send a copy of the file to bigquery
$ dbt seed


output:
======
$ dbt seed
20:04:32  Running with dbt=1.11.8
20:04:35  Registered adapter: bigquery=1.11.1
20:04:36  [WARNING]: Configuration paths exist in your dbt_project.yml file which do not apply to any resources.
There are 1 unused configuration paths:
- models.ai_analytics_lab.example
20:04:37  Found 1 seed, 539 macros
20:04:37
20:04:37  Concurrency: 1 threads (target='dev')
20:04:37
20:04:40  1 of 1 START seed file dbt_dev.orders .......................................... [RUN]
20:04:47  1 of 1 OK loaded seed file dbt_dev.orders ...................................... [INSERT 5 in 7.02s]
20:04:47
20:04:47  Finished running 1 seed in 0 hours 0 minutes and 9.95 seconds (9.95s).
20:04:47
20:04:47  Completed successfully
20:04:47
20:04:47  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=1


Check in bigquery inside ai-analytics-lab project for the table called orders
----

create a file stg_orders.sql inside models/staging/ folder with below view sql
select
    order_id,
    customer_id,
    order_date,
    amount
from {{ ref('orders') }}

----
send a copy of this file to create a view in bigquery
$ dbt run

output
======
$ dbt run
20:10:15  Running with dbt=1.11.8
20:10:17  Registered adapter: bigquery=1.11.1
20:10:18  [WARNING]: Configuration paths exist in your dbt_project.yml file which do not apply to any resources.
There are 1 unused configuration paths:
- models.ai_analytics_lab.example
20:10:18  Found 1 seed, 1 model, 539 macros
20:10:18
20:10:18  Concurrency: 1 threads (target='dev')
20:10:18
20:10:21  1 of 1 START sql view model dbt_dev.stg_orders ................................. [RUN]
20:10:23  1 of 1 OK created sql view model dbt_dev.stg_orders ............................ [CREATE VIEW (0 processed) in 2.26s]
20:10:24
20:10:24  Finished running 1 view model in 0 hours 0 minutes and 5.52 seconds (5.52s).
20:10:24
20:10:24  Completed successfully
20:10:24
20:10:24  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=1

Check in bigquery to find the stg_orders view

-------

GitHub for the first time set up:

$ git config --global user.name "Angeline-Paul"

$ git config --global user.email "angeline.juliette@gmail.com"

got to git hub and create a new repository called ai-analytics-lab without readme.md.
create the readme.md file in the local folder.
from the repository get the git remote command and run it in bash from inside /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab 

$ git remote add origin https://github.com/Angeline-Paul/ai-analytics-lab.git

set up generate token for ai-analytics-lab content-> read and write for 90 days
then commit the main and original:

$ git branch -M main
$ git push -u origin main

output:
=======
The project is now visible in GitHub.

-----
## Outcome

A working ELT pipeline:

orders (raw layer) → stg_orders (staging layer)

Both tables successfully created in Google BigQuery.

---

## Tools Used

- dbt (Core)
- Google BigQuery
- GitHub
- SQL

---

## Key Learnings

- dbt seed loads local CSV data into warehouse tables
- dbt run builds transformation models from staging SQL
- Importance of separating raw and staging layers
- First end-to-end pipeline execution successful

---

## Challenges Faced

- Initial confusion around Git/GitHub linking
- Understanding dbt project structure and execution flow

---

## Next Steps (Day 3)

- Build metrics layer (fct_revenue)
- Introduce business-level aggregation logic
- Improve model structure and naming conventions

## Date
23 April 2026
=============

orders → stg_orders → fct_revenue → validated

----
cd /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab
----
create a sql file models/marts/fct_revenue.sql
----
$ dbt run
16:56:46  Running with dbt=1.11.8
16:56:49  Registered adapter: bigquery=1.11.1
16:56:50  [WARNING]: Configuration paths exist in your dbt_project.yml file which do not apply to any resources.
There are 1 unused configuration paths:
- models.ai_analytics_lab.example
16:56:50  Found 1 seed, 2 models, 539 macros
16:56:50
16:56:50  Concurrency: 1 threads (target='dev')
16:56:50
16:56:53  1 of 2 START sql view model dbt_dev.stg_orders ................................. [RUN]
16:56:55  1 of 2 OK created sql view model dbt_dev.stg_orders ............................ [CREATE VIEW (0 processed) in 2.55s]
16:56:55  2 of 2 START sql view model dbt_dev.fct_revenue ................................ [RUN]
16:56:58  2 of 2 OK created sql view model dbt_dev.fct_revenue ........................... [CREATE VIEW (0 processed) in 2.16s]
16:56:58
16:56:58  Finished running 2 view models in 0 hours 0 minutes and 7.49 seconds (7.49s).
16:56:58
16:56:58  Completed successfully
16:56:58
16:56:58  Done. PASS=2 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=2

---

check in Bigquery. Validate by querying the new view


---
create YAML file called models/marts/schema.yml
YAML file contains metadata, documentation and testing

</> YAML file content
version: 2

models:
  - name: fct_revenue
    description: Daily revenue metrics aggregated by order_date
    columns:
      - name: order_date
        description: Date of the order
        tests:
          - not_null

      - name: total_revenue
        description: Total revenue per day

      - name: total_orders
        description: Number of orders per day

      - name: unique_customers
        description: Count of unique customers per day

---
test the data.

$ dbt test
17:36:10  Running with dbt=1.11.8
17:36:11  Registered adapter: bigquery=1.11.1
17:36:13  [WARNING]: Configuration paths exist in your dbt_project.yml file which do not apply to any resources.
There are 1 unused configuration paths:
- models.ai_analytics_lab.example
17:36:13  Found 1 seed, 2 models, 1 test, 539 macros
17:36:13
17:36:13  Concurrency: 1 threads (target='dev')
17:36:13
17:36:15  1 of 1 START test not_null_fct_revenue_order_date .............................. [RUN]
17:36:18  1 of 1 PASS not_null_fct_revenue_order_date .................................... [PASS in 3.56s]
17:36:18
17:36:18  Finished running 1 test in 0 hours 0 minutes and 5.20 seconds (5.20s).
17:36:18
17:36:18  Completed successfully
17:36:18
17:36:18  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=1

what testing is done:
=====================

Example (what dbt actually does behind the scenes)

Your YAML:

- name: order_date
  tests:
    - not_null

dbt converts this into something like:

select *
from fct_revenue
where order_date is null

If rows exist → ❌ test fails
If none → ✅ test passes

----

created a structured and presentable readme.md file and moved to GitHub

git add README.md
git commit -m "Refactor README with structured project documentation"
git push


## Date
28 April 2026
=============

orders → stg_orders → fct_revenue → dim_customer_metrics

----
cd /c/Angeline/dbt_project/ai_analytics_lab/ai_analytics_lab
----
create a sql file models/marts/dim_customer_metrics.sql


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
