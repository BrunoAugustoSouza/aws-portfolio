import os
from dotenv import load_dotenv
load_dotenv()

BUCKET_NAME = os.getenv("BUCKET_NAME")

DATABASE_NAME = "nyc_hvfhs_analytics_lakehouse"

ATHENA_OUTPUT = f"s3://{BUCKET_NAME}/athena-results/"
GOLD_PATH = f"s3://{BUCKET_NAME}/gold"
REGION = os.getenv("AWS_REGION")
PROMPT_SUGGEST_PATH = "prompts/suggested_queries.txt"
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
