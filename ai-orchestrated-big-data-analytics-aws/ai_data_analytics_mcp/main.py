import json
from dotenv import load_dotenv

from src.suggest_queries import suggest_queries
from src.athena_executor import execute_query
from src.utils import extract_external_location
from src.bucket_cleanse import delete_files

load_dotenv()


def run():

    print("\nAI Data Analytics MCP\n")

    suggestions = suggest_queries()

    print("\nAvailable analyses:\n")

    for item in suggestions:
        print(f"{item['id']} - {item['description']}")

    choice = int(input("\nChoose query number: "))

    selected = next(
        q for q in suggestions
        if q["id"] == choice
    )

    sql = selected["sql"]

    ctas = sql
    result_path = extract_external_location(ctas)
    relative_path = "gold/" + result_path.split("gold/")[-1]
    delete_files(result_path)

    query_id = execute_query(ctas)
    
    print("\nQuery executed!\n")

    print("SQL:")
    print(sql)

    print("\nS3 location:")
    print(result_path)

    print("\nAthena Query ID:")
    print(query_id)


if __name__ == "__main__":
    run()