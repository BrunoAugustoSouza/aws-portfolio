# 🚀 Serverless Data Lake Pipeline on AWS

![AWS](https://img.shields.io/badge/AWS-Serverless-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-623CE4)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Data%20Engineering](https://img.shields.io/badge/Data%20Engineering-Portfolio-success)
![Cost](https://img.shields.io/badge/Cost-Low%20(%3C$10%2Fmonth)-brightgreen)

------------------------------------------------------------------------

## 🧩 Business Problem It Solves

Many digital platforms (job marketplaces, e-commerce sites, fintech apps, SaaS products) generate large volumes of event data but struggle with:

- Monitoring trends in near real-time
- Calculating average prices or transaction values
- Tracking job postings and salary benchmarks
- Measuring event frequency and growth
- Enabling analysts to query data without engineering bottlenecks
- Keeping infrastructure costs under control

This project demonstrates how to build a scalable, cost-efficient analytics backbone to solve those problems.


# 📊 What Can Be Done With This Project?

Using this architecture, a company could:

## 💼 Job Market Monitoring

- Track number of job postings per day
- Monitor average salary by role, location, or seniority
- Identify demand trends for specific skills
- Detect sudden hiring spikes in certain industries

## 💰 Price & Revenue Analytics

- Calculate average transaction values
- Monitor revenue by event type
- Analyze user purchasing behavior
- Detect anomalies in transaction amounts

## 📈 Operational Monitoring

- Track daily event volume
- Monitor product engagement metrics
- Measure feature adoption
- Build dashboards for BI teams using Athena queries

## 🌍 Project Context

This project simulates a **production-ready, serverless data lake
architecture** designed for modern cloud-native companies in the US and
EU.

It demonstrates: - Event-driven ingestion - Columnar storage
optimization (Parquet) - Data cataloging - SQL analytics -
Infrastructure as Code (Terraform) - Cost-efficient serverless
architecture

------------------------------------------------------------------------

## 🏗 Architecture Diagram

![Architecture Diagram](architecture_diagram.png)

### 🔄 Data Flow

1.  JSON events land in **S3 Raw Layer**
2.  **S3 Event Trigger** invokes Lambda
3.  Lambda transforms JSON → Parquet
4.  Parquet stored in **S3 Processed Layer**
5.  Glue Data Catalog registers schema
6.  Athena enables SQL-based analytics

------------------------------------------------------------------------

## 🧠 Business Use Case

Simulates an **event-driven analytics pipeline** for a digital product
company tracking user transactions and engagement.

Example use cases: - Revenue tracking - Event frequency analysis -
Behavioral segmentation - Near real-time BI dashboards

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   Amazon S3 (Data Lake Storage)
-   AWS Lambda (Serverless ETL)
-   AWS Glue Data Catalog
-   Amazon Athena
-   IAM (Least Privilege)
-   Terraform (Infrastructure as Code)
-   Python (fastparquet)

------------------------------------------------------------------------

## 📊 Example Input Event

``` json
{
  "event_id": "evt_001",
  "user_id": "u123",
  "event_type": "purchase",
  "amount": 49.90,
  "event_timestamp": "2026-02-12T14:32:10Z"
}
```

------------------------------------------------------------------------

## 🔎 Example Athena Query

``` sql
SELECT 
  company, 
  COUNT(*) AS total_jobs
FROM job_analytics.jobs
GROUP BY company
ORDER BY total_jobs DESC
LIMIT 10;
```

------------------------------------------------------------------------

## 💰 Cost Efficiency

Designed for low-traffic portfolio deployment:

| Service              | Estimated Monthly Cost |
|----------------------|------------------------|
| Amazon S3            | < $2                   |
| AWS Lambda           | Free Tier              |
| Glue Data Catalog    | ~$1                    |
| Amazon Athena        | ~$1–2                  |
| **Total Estimated**  | **< $10/month**        |


------------------------------------------------------------------------

## 🛠 Engineering Practices Demonstrated

✔ Infrastructure as Code (Terraform)\
✔ Serverless-first architecture\
✔ Event-driven design\
✔ Columnar data optimization (Parquet)\
✔ Data lake layered modeling (raw → processed)\
✔ IAM least privilege\
✔ Cost-aware architecture decisions\
✔ Cloud-native analytics stack

------------------------------------------------------------------------

## 🎯 Why This Project Attracts International Recruiters

This portfolio project signals:

-   Real-world AWS architecture experience
-   Practical data modeling decisions
-   Understanding of cost-performance tradeoffs
-   DevOps + IaC maturity
-   Ability to design scalable, production-style systems

It aligns directly with requirements for **Mid-Level Cloud Data Engineer
roles** in international markets.

------------------------------------------------------------------------

## 🚀 Potential Enhancements

-   Partitioned Parquet by date
-   CloudWatch monitoring dashboard
-   CI/CD pipeline with GitHub Actions
-   Data quality validation layer
-   Step Functions orchestration

------------------------------------------------------------------------

## 👨‍💻 Author

AWS Data Engineering Portfolio Project\
Generated on: 2026-02
