import json
import urllib
import boto3
import os
from typing import List

BUCKET_NAME = os.getenv("BUCKET_NAME")

# Cliente S3 criado fora do handler (reutilização entre execuções)
s3_client = boto3.client("s3")


def upload_stream_to_s3(response_stream, bucket: str, key: str):
    s3_client.upload_fileobj(response_stream, bucket, key)


def download_trip_data_to_s3(year_month: List[str], prefix: str) -> List[str]:
    uploaded_files = []

    for ym in year_month:
        download_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_{ym}.parquet"
        s3_key = f"{prefix}/fhvhv_tripdata_{ym}.parquet"

        with urllib.request.urlopen(download_url, timeout=300) as response:
            if response.status != 200:
                raise Exception(f"Erro HTTP: {response.status}")
            # Upload direto do stream para S3
            upload_stream_to_s3(response, BUCKET_NAME, s3_key)

        uploaded_files.append(s3_key)

    return uploaded_files


def download_taxi_zone_lookup(prefix: str) -> str:
    download_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
    s3_key = f"{prefix}/taxi_zone_lookup.csv"

    with urllib.request.urlopen(download_url, timeout=300) as response:
            if response.status != 200:
                raise Exception(f"Erro HTTP: {response.status}")
            # Upload direto do stream para S3
            upload_stream_to_s3(response, BUCKET_NAME, s3_key)
            
    return s3_key


def lambda_handler(event, context):
    """
    Expected event:
    {
        "year_month": ["2026-01"],
        "trip_prefix": "raw/hvfhs",
        "lookup_prefix": "aux"
    }
    """

    try:
        year_month = event.get("year_month", ["2026-01"])
        trip_prefix = event.get("trip_prefix", "raw/hvfhs")
        lookup_prefix = event.get("lookup_prefix", "aux")

        trip_files = download_trip_data_to_s3(year_month, trip_prefix)
        lookup_file = download_taxi_zone_lookup(lookup_prefix)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Download and upload successful",
                "trip_files_uploaded": trip_files,
                "lookup_file_uploaded": lookup_file
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }