# 🚕 NYC TLC Big Data Analytics Platform

**EMR Serverless + Step Functions + Spark (Cost-Optimized Production
Architecture)**

------------------------------------------------------------------------

## 📌 Project Overview

This project demonstrates a **production-style big data analytics
platform** built using:

-   **Amazon EMR Serverless (Apache Spark)**
-   **AWS Step Functions (Workflow Orchestration)**
-   **Amazon S3 (Data Lake)**
-   **NYC TLC HVFHS Trip Data (Real-world dataset)**

The system processes large-scale ride-hailing trip data (Uber, Lyft,
Via, etc.) and produces a **single unified analytics table** optimized
for BI tools and downstream analytics.

Designed for: - Big Data Engineering roles - Data Platform Engineering -
Analytics Engineering - Cloud Data Architecture

------------------------------------------------------------------------

## 🏗️ Architecture

Raw Data (S3 Bronze) ↓ Spark Transformations (EMR Serverless) ↓ Curated
Analytics Table (S3 Silver/Gold) ↓ BI / Athena / Dashboard

Orchestrated with AWS Step Functions

------------------------------------------------------------------------

## 📊 Dataset

Source: NYC Taxi & Limousine Commission (TLC)

High Volume For-Hire Vehicle (HVFHS) trip records including: - Uber
(HV0003) - Lyft (HV0005) - Via (HV0004) - Juno (HV0002)

Schema includes: - Pickup & dropoff timestamps - Trip distance &
duration - Fare breakdown (tax, tolls, congestion fees, airport fees) -
Driver pay - Shared ride flags - Wheelchair accessibility indicators

------------------------------------------------------------------------

## 🔎 Key Business Questions Answered

The Spark pipeline generates a **unified analytics table** answering:

-   📈 Revenue by company (Uber vs Lyft vs Via)
-   🗓️ Peak demand hours & weekdays
-   🚗 Average trip distance and duration
-   💰 Driver earnings vs passenger fare trends
-   🏙️ Most profitable pickup/dropoff zones
-   🛫 Airport trip revenue impact
-   ♿ WAV (wheelchair-accessible vehicle) usage trends
-   👥 Shared ride penetration rate

------------------------------------------------------------------------

## 🧠 Data Engineering Highlights

✔ Partitioned by `year` and `month` for cost-efficient querying\
✔ Column pruning & optimized Spark transformations\
✔ EMR Serverless auto-scaling for minimal idle cost\
✔ Step Functions orchestration for production workflow\
✔ Designed to process large Parquet datasets efficiently

------------------------------------------------------------------------

## 💰 Cost Optimization Strategy

-   EMR Serverless (no idle cluster costs)
-   Auto-stop after job completion
-   Partitioned Parquet storage
-   No always-on infrastructure
-   Fully serverless orchestration

Estimated cost for demo-scale runs: **very low (few dollars per run)**

------------------------------------------------------------------------

## 🚀 How to Run

1.  Upload raw TLC data to S3
2.  Deploy Step Functions state machine
3.  Configure EMR Serverless application
4.  Trigger workflow execution
5.  Query curated analytics table via Athena or Spark

------------------------------------------------------------------------

## 📂 Output: Unified Analytics Table

Final dataset includes:

-   company_name
-   year, month, pickup_hour
-   total_trips
-   total_revenue
-   total_driver_pay
-   avg_trip_miles
-   avg_trip_minutes
-   shared_trip_rate
-   wav_trip_rate

Optimized for: - Power BI - Tableau - Amazon QuickSight - Athena SQL
queries

------------------------------------------------------------------------

## 🎯 Why This Project Stands Out for Recruiters

This project demonstrates:

-   Real-world large dataset processing
-   Serverless big data architecture
-   Production-style orchestration
-   Cost-aware engineering decisions
-   Scalable Spark transformation design
-   Business-oriented analytics modeling

It shows both **technical depth** and **architectural maturity**.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   AWS EMR Serverless
-   Apache Spark (PySpark)
-   AWS Step Functions
-   Amazon S3
-   NYC TLC Open Data

------------------------------------------------------------------------

## 📌 Future Enhancements

-   Add incremental processing (monthly partitions)
-   Add data quality checks
-   Implement CI/CD for Spark jobs
-   Add dashboard layer
-   Integrate data catalog automation

------------------------------------------------------------------------

## 👤 Author

Big Data Engineering Portfolio Project\
Focused on scalable, serverless, cost-efficient cloud data platforms.
