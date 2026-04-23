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