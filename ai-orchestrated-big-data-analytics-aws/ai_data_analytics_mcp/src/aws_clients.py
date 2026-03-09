import boto3
import os
from src.config import REGION, AWS_ACCESS_KEY, AWS_SECRET

def get_glue_client():

    return boto3.client(
        "glue",
        region_name=REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET
    )

def get_s3_resource():
    return boto3.resource(
        "s3",
        region_name=REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET
    )

def get_athena_client():

    return boto3.client(
        "athena",
        region_name=REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET
    )