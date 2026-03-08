import os
from dotenv import load_dotenv

DATABASE_NAME = "nyc_taxi_analytics_lakehouse"
BUCKET_NAME = "ai-bigdata-lakehouse"

ATHENA_OUTPUT = f"s3://{BUCKET_NAME}/athena-temp/"
GOLD_PATH = f"s3://{BUCKET_NAME}/gold/analytics/"
REGION = "us-east-1"
PROMPT_SQL_PATH = "prompts/generate_sql_prompt.txt"
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")