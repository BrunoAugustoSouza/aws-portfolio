<!-- ===================== BADGES ===================== -->

<p align="center">

<img src="https://img.shields.io/badge/AWS-Cloud%20Data%20Engineering-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-Data%20Pipelines-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Architecture-Serverless-34A853?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Infrastructure-Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white"/>
<img src="https://img.shields.io/badge/Data%20Lake-S3%20Architecture-569A31?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Big%20Data-Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white"/>

</p>

---

# 🚀 AWS Data Engineering Portfolio

Production-oriented **AWS Data Engineering projects** demonstrating how modern data platforms are built in **cloud-native environments**.

Focus areas:

- **ETL / ELT pipelines**
- **Serverless data platforms**
- **Big data processing**
- **Data lake architecture**
- **Infrastructure as Code**
- **Cost-efficient cloud analytics**

Designed to simulate **real-world architectures used by global tech companies.**

---

# 🎯 Portfolio Goals

This repository demonstrates practical experience building **scalable cloud data systems** using AWS.

Each project emphasizes:

✔ Scalable architectures  
✔ Production-grade pipelines  
✔ Cost-efficient serverless design  
✔ Infrastructure automation  
✔ Clean Python engineering  

---

# 🧰 Core Tech Stack

### ☁️ Cloud Platform

![AWS](https://img.shields.io/badge/Amazon_Web_Services-Cloud_Platform-FF9900?style=flat&logo=amazonaws)

### 🧠 Data Engineering

![Spark](https://img.shields.io/badge/Apache_Spark-Big_Data-E25A1C?style=flat&logo=apachespark)
![ETL](https://img.shields.io/badge/ETL-Pipelines-blue?style=flat)
![DataLake](https://img.shields.io/badge/Data_Lake-S3-green?style=flat)

### ⚙️ Infrastructure

![Terraform](https://img.shields.io/badge/Terraform-Infrastructure_as_Code-623CE4?style=flat&logo=terraform)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=flat&logo=docker)

### 🗄️ Storage & Databases

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Relational_DB-316192?style=flat&logo=postgresql)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL_DB-4053D6?style=flat&logo=amazondynamodb)

### 🧪 Programming

![Python](https://img.shields.io/badge/Python-Data_Engineering-3776AB?style=flat&logo=python)
![SQL](https://img.shields.io/badge/SQL-Analytics-blue?style=flat)

---

# 📂 Featured Projects

---

# 🧠 AI-Orchestrated Big Data Analytics Pipeline

End-to-end **serverless big data pipeline** processing real-world ride-sharing datasets.

### Architecture


```mermaid
flowchart LR

subgraph Ingestion
A[EventBridge<br>Scheduler]
B[AWS Lambda<br>Raw Data Collector]
end

subgraph DataLake
C[S3 Data Lake<br>Bronze Layer]
F[S3 Curated Data<br>Silver Layer]
K[S3 Analytics Tables<br>Gold Layer]
end

subgraph Processing
D[EMR Serverless<br>Spark Processing]
end

subgraph AI
I[AI Analytics Engine<br>MCP + LLM]
end

A --> B
B --> C
C --> D
D --> F
F --> I
I --> K

```


### Technologies

![Lambda](https://img.shields.io/badge/AWS_Lambda-Serverless-FF9900?style=flat&logo=awslambda)
![S3](https://img.shields.io/badge/Amazon_S3-Data_Lake-569A31?style=flat&logo=amazons3)
![EMR](https://img.shields.io/badge/EMR_Serverless-Spark_Processing-FF9900?style=flat)
![StepFunctions](https://img.shields.io/badge/Step_Functions-Orchestration-FF9900?style=flat)
![Glue](https://img.shields.io/badge/AWS_Glue-Data_Catalog-FF9900?style=flat)
![Athena](https://img.shields.io/badge/Athena-Serverless_SQL-FF9900?style=flat)
![Terraform](https://img.shields.io/badge/Terraform-IaC-623CE4?style=flat)

### Dataset

**NYC Taxi & Limousine Commission – HVFHS**

Ride-sharing trip data from:

- Uber
- Lyft
- Via
- Juno

Includes:

- trip distance
- timestamps
- fare breakdown
- driver earnings
- shared rides
- wheelchair accessibility

---

### Analytics Produced

The pipeline generates analytics answering:

📈 Revenue by company  
🗓️ Peak demand hours  
🚗 Average trip distance & duration  
💰 Driver earnings vs fares  
🏙️ Most profitable zones  
🛫 Airport trip impact  
♿ Accessibility usage  
👥 Shared ride adoption  

---

### Engineering Highlights

✔ **Partitioned Parquet datasets** (`year/month`)  
✔ **Spark optimizations** with column pruning  
✔ **Serverless EMR autoscaling**  
✔ **Step Functions orchestration**  
✔ **Glue metadata catalog**  
✔ **Athena analytics queries**  
✔ **AI-assisted data exploration**

📖 Project details →  
`ai-orchestrated-big-data-analytics-aws/README.md`

---

# 🤖 AI Data Lake Analytics Engine

Experimental **AI-driven data analytics layer** using **AWS MCP + LLM integration**.

### Workflow

1️⃣ Read table metadata from **Glue Catalog**  
2️⃣ AI suggests possible analytics queries  
3️⃣ User selects the analysis  
4️⃣ System generates **Gold Layer datasets**

Output:

**Analytics tables automatically generated in Parquet.**

📖 Documentation →  
`ai_data_analytics_mcp/README_AI_MCP_Lakehouse.md`

---

# ⚙️ Infrastructure as Code

Entire platform provisioned using **Terraform**.

Includes:

- Data Lake infrastructure
- EMR Serverless environment
- Step Functions workflows
- Glue Data Catalog
- IAM roles & permissions
- Lambda ingestion

Benefits:

✔ Fully reproducible infrastructure  
✔ Version-controlled cloud architecture  
✔ Fast environment deployment  

---

# 💰 Cost Optimization Strategy

All architectures prioritize **low operational cost**.

Techniques applied:

- Serverless compute
- No always-on clusters
- Partitioned Parquet storage
- Auto-scaling Spark workloads
- S3 lifecycle management

**Demo pipeline run cost:**  
≈ **$0.04 per execution**

---

# 📊 Engineering Practices Demonstrated

- Data lake architecture
- Partitioned storage design
- Idempotent ETL pipelines
- Event-driven workflows
- Cloud monitoring & logging
- Infrastructure modularization
- Security best practices (IAM least privilege)

---

# 🎯 Target Roles

This portfolio is focused on roles such as:

- **AWS Data Engineer**
- **Cloud Data Engineer**
- **Data Platform Engineer**
- **Big Data Engineer**
- **Analytics Engineer**

---

# 📬 Contact

**LinkedIn**  
https://www.linkedin.com/in/brunoaugustosouza/

**Email**  
bruno.augusto.souza@outlook.com

**Phone**  
+55 (11) 97298-3578 ([Call me on Whatsapp](https://wa.me/5511972983578))

---

⭐ If you are a recruiter or hiring manager looking for **AWS-focused Data Engineers**, feel free to explore the projects.