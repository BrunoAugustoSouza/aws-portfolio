import boto3
import os

BUCKET_NAME = os.getenv("BUCKET_NAME")

athena = boto3.client("athena")

DATABASE = "hvfhs_db"
TABLE = "hvfhs_analytics_mart"
OUTPUT = f"s3://{BUCKET_NAME}/athena-results/"

def run_query(sql):
    response = athena.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={"Database": DATABASE},
        ResultConfiguration={"OutputLocation": OUTPUT}
    )
    return f"Query started: {response['QueryExecutionId']}"