# 🚀 AWS Data Pipeline Deployment Guide (Terraform)

This document explains how to deploy the complete AWS serverless data
pipeline infrastructure using Terraform.

The project provisions:

-   S3 buckets (raw + processed layers)
-   IAM roles and policies
-   AWS Lambda function
-   Event triggers (S3 → Lambda)
-   Optional Glue Catalog resources

------------------------------------------------------------------------

# 📋 Prerequisites

## Lambda layer

Take this steps on [how to create](LAYER_CREATION.md) a lambda layer with the necessaries requirements


## 1️⃣ AWS Account

An active AWS account with permissions to create: - S3 - IAM - Lambda -
Glue (optional)

## 2️⃣ Installed Tools

### Terraform (\>= 1.5)

``` bash
terraform -version
```

Download: https://developer.hashicorp.com/terraform/downloads

### AWS CLI

``` bash
aws --version
```

Configure credentials:

``` bash
aws configure
```

Provide: - AWS Access Key - AWS Secret Key - Default region (e.g.,
us-east-1) - Output format: json

------------------------------------------------------------------------

# 📁 Project Structure

    terraform/
    │
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    ├── provider.tf
    ├── terraform.tfvars

------------------------------------------------------------------------

# ⚙️ Step 1 --- Configure Variables

Open:

    terraform.tfvars

Example:

``` hcl
project_name = "aws-data-pipeline"
environment  = "dev"
aws_region   = "us-east-1"

raw_bucket_name       = "my-raw-data-bucket-123"
processed_bucket_name = "my-processed-data-bucket-123"

lambda_function_name = "data-processing-lambda"
```

Important: S3 bucket names must be globally unique.

------------------------------------------------------------------------

# 🔍 Step 2 --- Initialize Terraform

Inside the `terraform/` folder:

``` bash
terraform init
```

This will: - Download AWS provider - Create `.terraform/` folder -
Initialize backend (local state by default)

------------------------------------------------------------------------

# 🧠 Step 3 --- Validate Configuration

``` bash
terraform validate
```

Checks for syntax errors.

------------------------------------------------------------------------

# 📊 Step 4 --- Preview Infrastructure Plan

``` bash
terraform plan
```

Terraform will show:

-   Resources to be created
-   Resources to be modified
-   Resources to be destroyed

Nothing is deployed yet.

------------------------------------------------------------------------

# 🚀 Step 5 --- Deploy Infrastructure

``` bash
terraform apply
```

Type:

    yes

Terraform will:

-   Create S3 buckets
-   Create IAM roles
-   Deploy Lambda function
-   Configure permissions
-   Connect S3 trigger to Lambda

Deployment usually takes 1--3 minutes.

------------------------------------------------------------------------

# ✅ Step 6 --- Verify Deployment

Check in AWS Console:

-   S3 → Buckets created
-   Lambda → Function deployed
-   IAM → Role attached
-   S3 → Event notification configured

Test by uploading a file to the raw bucket.

------------------------------------------------------------------------

# 🧹 Step 7 --- Destroy Infrastructure (Optional)

To remove all resources:

``` bash
terraform destroy
```

Confirm with:

    yes

------------------------------------------------------------------------

# 🏗️ Infrastructure Overview

This Terraform project creates:

  Resource              Purpose
  --------------------- ------------------------------
  S3 Raw Bucket         Stores incoming data
  S3 Processed Bucket   Stores Parquet files
  IAM Role              Grants Lambda permissions
  Lambda Function       Processes CSV → Parquet
  S3 Trigger            Automatically invokes Lambda


------------------------------------------------------------------------

# 📦 Useful Terraform Commands

Format code:

``` bash
terraform fmt
```

Show current state:

``` bash
terraform show
```

List resources:

``` bash
terraform state list
```

------------------------------------------------------------------------

# 📈 Resume Example

Designed and deployed a serverless data processing pipeline on AWS using
Terraform, integrating S3, Lambda, and IAM to automate CSV-to-Parquet
transformation with event-driven architecture.