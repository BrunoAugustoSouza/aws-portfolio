import json
import os
import logging
from datetime import datetime
import requests
import boto3
import pandas as pd
import io

# Configure structured logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

BUCKET_NAME = os.environ.get("BUCKET_NAME")
SOURCE_NAME = os.environ.get("SOURCE_NAME", "themuse")

API_URL = "https://www.themuse.com/api/public/jobs"

def transform_jobs(data, ingestion_time):
    records = []

    for job in data.get("results", []):
        records.append({
            "job_id": job.get("id"),
            "title": job.get("name"),
            "company": job.get("company", {}).get("name"),
            "location": job.get("locations")[0]["name"] if job.get("locations") else None,
            "level": job.get("levels")[0]["name"] if job.get("levels") else None,
            "publication_date": job.get("publication_date"),
            "landing_page": job.get("refs", {}).get("landing_page"),
            "ingestion_timestamp": ingestion_time.isoformat()
        })

    return pd.DataFrame(records)

def lambda_handler(event, context):
    try:
        logger.info("Starting job ingestion from The Muse API")

        # Fetch data (1 page per execution for cost control)
        params = {"page": 1}
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        ingestion_time = datetime.now()
        year = ingestion_time.strftime("%Y")
        month = ingestion_time.strftime("%m")
        day = ingestion_time.strftime("%d")
        timestamp_str = ingestion_time.strftime("%Y%m%d_%H%M%S")

        s3_key = (
            f"raw/source={SOURCE_NAME}/"
            f"year={year}/month={month}/day={day}/"
            f"jobs_{timestamp_str}.json"
        )

        payload = {
            "ingestion_timestamp": ingestion_time.isoformat(),
            "source": SOURCE_NAME,
            "api_page": 1,
            "results_count": len(data.get("results", [])),
            "data": data
        }

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=s3_key,
            Body=json.dumps(payload),
            ContentType="application/json"
        )

        logger.info(f"Successfully saved raw data to s3://{BUCKET_NAME}/{s3_key}")

        df = transform_jobs(data, ingestion_time)

        buffer = io.BytesIO()
        df.to_parquet(buffer, index=False, engine='fastparquet')

        curated_key = (
            f"curated/year={year}/month={month}/"
            f"jobs_{timestamp_str}.parquet"
        )

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=curated_key,
            Body=buffer.getvalue()
        )

        logger.info(f"Successfully saved curated data to s3://{BUCKET_NAME}/{curated_key}")


        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Ingestion successful",
                "records": payload["results_count"],
                "s3_path": s3_key
            })
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise
