import boto3
from src.aws_clients import get_s3_resource
from src.config import BUCKET_NAME

s3 = get_s3_resource()
bucket = s3.Bucket(BUCKET_NAME)

def delete_files(bucket_prefix:str):
    bucket.objects.filter(Prefix=bucket_prefix).delete()
    
    return None