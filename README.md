![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Python](https://img.shields.io/badge/Python-Data%20Engineering-blue)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-green)


# 🚀 AWS Data Engineering Portfolio

Production-oriented **AWS Data Engineering projects** designed to simulate real-world architectures used in international tech companies.

This repository demonstrates hands-on experience with scalable data pipelines, serverless processing, data lakes, real-time ingestion, and cloud-native analytics solutions built on AWS.

---

## 🎯 Objective

To showcase practical, cost-efficient, and production-ready AWS data engineering solutions aligned with global hiring standards (US/EU market).

Each project emphasizes:

- Scalability
- Reliability
- Cost optimization
- Infrastructure best practices
- Clear architecture documentation
- Clean and modular code

---

## 🏗️ Core Technologies

- **AWS S3** – Data Lake Storage  
- **AWS Lambda** – Serverless processing  
- **AWS Glue** – ETL & Data Catalog  
- **AWS Kinesis / Firehose** – Real-time ingestion  
- **Amazon Redshift** – Data Warehouse  
- **Amazon Athena** – Serverless querying  
- **Amazon RDS (PostgreSQL)** – Relational storage  
- **DynamoDB** – NoSQL storage  
- **AWS IAM** – Security & access control  
- **Amazon CloudWatch** – Monitoring & logging  
- **Terraform / CloudFormation** – Infrastructure as Code  
- **Python (Boto3, Pandas, PySpark)**  
- **SQL**

---

## 📂 Projects

![Architecture Diagram](job-market-analytics/architecture_diagram.png)

**Key Features**

- Near real-time ingestion
- Event-driven architecture
- Partitioned data lake design
- Cost-optimized storage
- Cloud-native monitoring

Read more about this project [here](job-market-analytics/README.md)

---

## 🧠 AI-Powered Big Data Analytics Pipeline (AWS)

**End-to-end serverless data engineering pipeline** processing large-scale ride-sharing trip datasets using AWS cloud-native services.

### Architecture

Raw Data → **S3 Bronze Layer** → **Spark Transformations (EMR Serverless)** → **Silver Layer** → **AI-powered analytics (MCP + LLM)** → **Gold Layer**

### Technologies

- AWS Lambda
- Amazon S3 (Data Lake)
- Amazon EMR Serverless (Apache Spark)
- AWS Step Functions (Workflow Orchestration)
- AWS Glue Data Catalog
- AWS Athena
- Terraform (Infrastructure as Code)
- AWS MCP integrated with AI for analytics automation

### Dataset

**NYC Taxi & Limousine Commission – HVFHS Trip Data**

Includes ride-sharing data from:

- Uber
- Lyft
- Via
- Juno

Trip records include:

- Pickup and dropoff timestamps
- Trip distance and duration
- Fare breakdown
- Driver pay
- Shared ride indicators
- Wheelchair accessibility flags

### Key Analytics Questions Answered

The pipeline generates a **unified analytics dataset** answering:

- 📈 Revenue comparison across ride-hailing companies
- 🗓️ Peak demand hours and busiest weekdays
- 🚗 Average trip distance and duration
- 💰 Driver earnings vs passenger fare trends
- 🏙️ Most profitable pickup and dropoff zones
- 🛫 Airport trip revenue impact
- ♿ Wheelchair-accessible vehicle usage
- 👥 Shared ride penetration rates

### Data Engineering Highlights

- Partitioned Parquet data (`year`, `month`) for **cost-efficient querying**
- **Apache Spark transformations** optimized with column pruning
- **EMR Serverless auto-scaling** to eliminate idle cluster costs
- **AWS Step Functions orchestration** for production-style pipelines
- Automated **metadata cataloging with AWS Glue**
- SQL analytics using **AWS Athena**
- AI-driven **query generation and analytics automation**

### Cost Optimization Strategy

Designed as a **fully serverless big data architecture**.

- No always-on clusters
- Auto-scaling Spark compute
- Partitioned Parquet storage
- Serverless workflow orchestration

Estimated demo run cost:

**~$0.04 per pipeline execution**

### ⚙️ Infrastructure as Code Data Platform

Provisioned the entire data platform above using **Terraform**.

Infrastructure includes:

- Data lake storage
- Spark compute environment
- Step Functions orchestration
- Glue catalog
- IAM roles and permissions
- Lambda ingestion pipeline

Benefits:

- Fully reproducible infrastructure
- Version-controlled cloud architecture
- Rapid environment provisioning

Read more about this project [here](ai-orchestrated-big-data-analytics-aws/README.md)

---

## 🤖 AI-Powered Data Analytics Layer

Built an experimental **AI-assisted analytics layer** using **AWS MCP + LLM integration**.

Workflow:

1. Python application reads the **Glue catalog table**
2. AI suggests **analytics queries automatically**
3. User selects the analysis
4. The system generates a **Gold Layer analytics dataset (Parquet)**

Goal:

Enable **AI-assisted data exploration on top of data lakes**.

Read more about this project [here](ai-orchestrated-big-data-analytics-aws/ai_data_analytics_mcp/README_AI_MCP_Lakehouse.md)

---


## 💰 Cost Optimization Focus

All projects are designed to:

- Run within AWS Free Tier (when possible)
- Use serverless services to reduce operational overhead
- Minimize idle compute costs
- Apply S3 lifecycle policies

---

## 📊 Engineering Principles Applied

- Data partitioning strategy
- Schema evolution awareness
- Idempotent pipeline design
- Event-driven architecture
- Infrastructure modularization
- Cost-performance trade-offs
- Security best practices (IAM roles, least privilege)

--

## 🧠 What This Repository Demonstrates

✔ Real-world cloud data architecture design  
✔ Strong AWS ecosystem knowledge  
✔ Production mindset (monitoring, logging, security)  
✔ Clean Python engineering practices  
✔ SQL optimization awareness  
✔ Data modeling fundamentals  

---

## 🌍 Target Roles

- AWS Data Engineer  
- Cloud Data Engineer  
- Analytics Engineer  
- Data Platform Engineer  
- Big Data Engineer  

---

## 📬 Contact

If you're a recruiter or hiring manager and would like to discuss my experience or projects:

- LinkedIn: https://www.linkedin.com/in/brunoaugustosouza/
- Email: bruno.augusto.souza@outlook.com
- Cel: +55(11)97298-3578

---

