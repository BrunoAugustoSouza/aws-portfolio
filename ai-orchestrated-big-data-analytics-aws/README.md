# AI-Orchestrated Big Data Analytics Pipeline (AWS)

## Overview

This project demonstrates a **production-style, serverless big data
analytics pipeline** built on AWS.

It processes large-scale ride-sharing trip datasets using a **modern
Data Lake architecture (Bronze → Silver → Gold)** and integrates
**AI-assisted analytics using AWS MCP + LLMs**.

The goal of this project is to simulate how **modern cloud data
platforms are built in real-world tech companies**, focusing on:

-   Scalable data pipelines
-   Serverless big data processing
-   Data lake architecture
-   Infrastructure as Code
-   Cost-efficient analytics platforms

------------------------------------------------------------------------

# Architecture

Data flows through a multi-layer **lakehouse-style pipeline**.

Raw Data (Lambda ingestion) → S3 Data Lake (Bronze Layer) → Apache Spark Transformations (EMR Serverless) → Curated Dataset (Silver Layer) → AI-Powered Analytics Engine (MCP + LLM) → Analytics Tables (Gold Layer)

------------------------------------------------------------------------

# Core Technologies

### AWS Services

-   AWS Lambda -- Data ingestion
-   Amazon S3 -- Data lake storage
-   Amazon EMR Serverless -- Distributed Spark processing
-   AWS Step Functions -- Workflow orchestration
-   AWS Glue -- Data catalog & crawler
-   AWS Athena -- Serverless SQL analytics

### Data Engineering Stack

-   Python
-   Apache Spark
-   PySpark
-   SQL
-   Parquet data format

### Infrastructure

-   Terraform (Infrastructure as Code)

### AI Integration

-   AWS MCP
-   LLM-assisted analytics generation

------------------------------------------------------------------------

# Dataset

Source:

NYC Taxi & Limousine Commission (TLC)

Dataset:

**High Volume For-Hire Vehicle (HVFHS) trip records** including:

-   Uber (HV0003)
-   Lyft (HV0005)
-   Via (HV0004)
-   Juno (HV0002)

Trip schema includes:

-   Pickup & dropoff timestamps
-   Trip distance
-   Trip duration
-   Fare breakdown
-   Driver pay
-   Shared ride flags
-   Wheelchair accessibility indicators

------------------------------------------------------------------------

# Pipeline Workflow

The entire pipeline is orchestrated using **AWS Step Functions**.

## Step 1 --- Data Ingestion

A **Lambda function downloads raw trip datasets** and stores them in:

S3 Bronze Layer

## Step 2 --- Spark Processing

An **EMR Serverless Spark job** performs:

-   Data cleaning
-   Feature engineering
-   Aggregations
-   Partitioning by year and month

Output:

S3 Silver Layer (Parquet)

## Step 3 --- Metadata Catalog

AWS Glue Crawler automatically:

-   Detects schema
-   Updates the Data Catalog
-   Enables SQL querying

## Step 4 --- Analytics Query Layer

Athena queries enable exploration of the dataset.

## Step 5 --- AI-Powered Analytics

A separate Python application integrates **AWS MCP + LLM** to:

1.  Read Glue Catalog tables
2.  Suggest business analytics queries
3.  Allow the user to select insights
4.  Automatically generate **Gold Layer datasets**

------------------------------------------------------------------------

# Business Questions Answered

The pipeline produces analytics such as:

-   Revenue comparison across ride-sharing companies
-   Peak demand hours and weekdays
-   Average trip distance and duration
-   Driver earnings vs passenger fares
-   Most profitable pickup and dropoff zones
-   Airport trip revenue impact
-   Wheelchair-accessible vehicle usage trends
-   Shared ride adoption rates

------------------------------------------------------------------------

# Data Engineering Highlights

-   Partitioned Parquet datasets
-   Spark transformations optimized with column pruning
-   EMR Serverless auto-scaling
-   Serverless workflow orchestration
-   Glue metadata catalog automation
-   SQL analytics via Athena
-   AI-assisted analytics generation

------------------------------------------------------------------------

# Cost Optimization Strategy

The architecture is designed to minimize cloud costs.

Techniques used:

-   Serverless Spark processing
-   No always-on clusters
-   Partitioned Parquet storage
-   On-demand compute
-   Auto-scaling workloads

Estimated demo pipeline cost:

≈ **\$0.04 per run**

------------------------------------------------------------------------

# Infrastructure Deployment

Infrastructure is provisioned using **Terraform**.

To deploy:

``` bash
cd terraform
terraform init
terraform apply
```

This creates:

-   Data Lake (S3)
-   EMR Serverless application
-   Lambda ingestion function
-   Step Functions workflow
-   Glue crawler
-   IAM roles

------------------------------------------------------------------------

# Running the Pipeline

After infrastructure deployment:

1.  Open **AWS Step Functions**
2.  Run the state machine
3.  The pipeline will automatically:

-   Ingest raw data
-   Run Spark transformations
-   Update Glue catalog
-   Prepare the dataset for analytics

------------------------------------------------------------------------

# AI Analytics Layer

Inside the project directory:

    ai_data_analytics_mcp/

Run:

``` bash
uv run main.py
```

The system will:

1.  Read the Glue catalog
2.  Suggest analytics queries using AI
3.  Let the user select insights
4.  Generate **Gold Layer Parquet datasets**

P.S. to install uv read more about it on this (documentation)[docs/uv_instalation.md]

------------------------------------------------------------------------

# Engineering Principles

This project demonstrates:

-   Data lake architecture design
-   Distributed data processing
-   Cloud-native pipelines
-   Infrastructure as Code
-   Scalable analytics platforms
-   Cost-efficient serverless architecture

------------------------------------------------------------------------

# Author

Bruno Augusto Souza

LinkedIn: https://www.linkedin.com/in/brunoaugustosouza/

Email: bruno.augusto.souza@outlook.com
