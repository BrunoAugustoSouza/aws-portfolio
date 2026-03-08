# AI Data Analytics MCP with AWS Lakehouse

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![AWS](https://img.shields.io/badge/AWS-Lakehouse-orange)
![LangChain](https://img.shields.io/badge/LangChain-AI%20Agent-green)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-black)
![Athena](https://img.shields.io/badge/AWS-Athena-232F3E)
![Glue](https://img.shields.io/badge/AWS-Glue-FF9900)
![S3](https://img.shields.io/badge/AWS-S3-569A31)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

------------------------------------------------------------------------

# AI Data Analytics MCP

This project implements an **AI-powered MCP (Multi-step Control
Process)** that allows users to explore and analyze a data lake using
**natural language queries**.

The system acts as an **AI Data Copilot** that automatically:

-   Reads metadata from the **AWS Glue Data Catalog**
-   Understands available datasets
-   Generates SQL queries with AI
-   Executes queries in **Amazon Athena**
-   Saves analytics datasets into the **Gold layer of a Data Lake**

This demonstrates how **AI agents can automate data analytics workflows
on modern lakehouse architectures.**

------------------------------------------------------------------------

# Architecture Overview

The system is built on top of a modern **AWS Lakehouse architecture**.

Core technologies:

-   AWS Glue (Data Catalog metadata)
-   Amazon Athena (serverless SQL engine)
-   Amazon S3 (data lake storage)
-   LangChain (AI agent orchestration)
-   OpenAI (LLM SQL generation)

------------------------------------------------------------------------

# Medallion Data Lake Architecture

    S3 Data Lake
    │
    ├── bronze/      raw ingestion data
    ├── silver/      cleaned and structured data
    └── gold/        AI-generated analytics datasets

The MCP generates **Gold datasets automatically** using Athena CTAS
queries.

------------------------------------------------------------------------

# Visual Architecture

``` mermaid
flowchart TD

User["User (Natural Language Request)"]
Agent["AI Agent (LangChain MCP)"]
Glue["AWS Glue Catalog"]
Athena["Amazon Athena"]
S3["Amazon S3 Data Lake"]

User --> Agent
Agent --> Glue
Glue --> Agent
Agent --> Athena
Athena --> S3
```

------------------------------------------------------------------------

# How It Works

The MCP agent executes the following workflow:

``` mermaid
sequenceDiagram

participant User
participant MCP
participant Glue
participant Athena
participant S3

User->>MCP: Natural language request
MCP->>Glue: Retrieve table metadata
Glue-->>MCP: Available tables + schema
MCP->>MCP: Generate SQL with AI
MCP->>Athena: Execute CTAS query
Athena->>S3: Save dataset to Gold Layer
S3-->>User: Query result available
```

Step-by-step:

1.  User asks a question using natural language.
2.  The MCP agent queries the **Glue Data Catalog** to retrieve tables
    and schemas.
3.  The metadata is injected into a **prompt template**.
4.  The AI model generates a valid **Athena SQL query**.
5.  The query is wrapped into a **CTAS statement**.
6.  Athena executes the query.
7.  The result is stored as a **new dataset in the Gold layer**.

------------------------------------------------------------------------

# Example Workflow

User request:

    Show the top 10 pickup zones by number of trips

Generated SQL:

``` sql
SELECT
pickup_location_id,
COUNT(*) AS trips
FROM silver_trip_data
GROUP BY pickup_location_id
ORDER BY trips DESC
LIMIT 10
```

Converted CTAS query:

``` sql
CREATE TABLE ai_generated_dataset
WITH (
 format='PARQUET',
 external_location='s3://<BUCKET_NAME>/gold/analytics/ai_generated_dataset/'
)
AS
SELECT ...
```

Result dataset:

    s3://<BUCKET_NAME>/gold/analytics/ai_generated_dataset/

------------------------------------------------------------------------

# Project Structure

    mcp_ai_analytics/
    │
    ├── main.py
    ├── config.py
    ├── aws_clients.py
    ├── glue_metadata.py
    ├── athena_tools.py
    ├── sql_generator.py
    │
    ├── prompts/
    │     generate_sql.txt
    │
    ├── .env
    └── requirements.txt

------------------------------------------------------------------------

# Configuration

Before running the project, configure the required environment
variables.

## .env File

Create a `.env` file in the root directory.

    AWS_ACCESS_KEY_ID=your_access_key
    AWS_SECRET_ACCESS_KEY=your_secret_key
    AWS_REGION=us-east-1

    OPENAI_API_KEY=your_openai_api_key

------------------------------------------------------------------------

# Required AWS Resources

The following AWS services must be configured.

## 1. S3 Data Lake

Example structure:

    s3://<BUCKET_NAME>/

    bronze/
    silver/
    gold/
    gold/analytics/
    athena-temp/

Athena query results location:

    s3://<BUCKET_NAME>/athena-temp/

------------------------------------------------------------------------

## 2. Glue Data Catalog

Example database:

    nyc_taxi_analytics_lakehouse

Tables should point to datasets in the **Silver layer**.

------------------------------------------------------------------------

## 3. Athena

Athena must be configured with:

-   the same Glue Catalog database
-   query results output location

Example:

    s3://<BUCKET_NAME>/athena-temp/

------------------------------------------------------------------------

# IAM Permissions Required

The IAM user running the MCP locally needs the following permissions:

-   Glue metadata access
-   Athena query execution
-   S3 read/write

Example IAM Policy:

``` json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase",
        "glue:GetTables",
        "glue:GetTable",
        "glue:GetPartitions",
        "glue:CreateTable"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "athena:StartQueryExecution",
        "athena:GetQueryExecution",
        "athena:GetQueryResults"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket",
        "s3:GetBucketLocation",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::<BUCKET_NAME>",
        "arn:aws:s3:::<BUCKET_NAME>/*"
      ]
    }
  ]
}
```

------------------------------------------------------------------------

# Running the Project

Install dependencies:

    pip install -r requirements.txt

Run the MCP:

    python main.py

Example prompt:

    Show total revenue per day

The MCP agent will:

1.  Discover available datasets
2.  Generate SQL automatically
3.  Execute the query in Athena
4.  Save the result in the **Gold layer**

------------------------------------------------------------------------

# Security

Never commit credentials to GitHub.

Add to `.gitignore`:

    .env

------------------------------------------------------------------------

# Future Improvements

Possible upgrades:

-   Query optimization with AI
-   Chart generation automatically
-   Dashboard creation
-   Semantic data layer
-   RAG with schema + sample data
-   Autonomous data exploration agent

------------------------------------------------------------------------

# Author

AI-powered Data Engineering Lakehouse project demonstrating:

-   AI-driven analytics
-   AWS Lakehouse architecture
-   LangChain AI agents
-   Automated SQL generation
