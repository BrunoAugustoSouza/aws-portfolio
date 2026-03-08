import time
from aws_clients import get_athena_client
from config import DATABASE_NAME, ATHENA_OUTPUT

athena = get_athena_client()

def execute_query(sql):

    response = athena.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={
            "Database": DATABASE_NAME
        },
        ResultConfiguration={
            "OutputLocation": ATHENA_OUTPUT
        }
    )

    query_id = response["QueryExecutionId"]

    while True:

        result = athena.get_query_execution(
            QueryExecutionId=query_id
        )

        state = result["QueryExecution"]["Status"]["State"]

        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break

        time.sleep(3)

    if state != "SUCCEEDED":
        raise Exception(f"Athena query failed: {state}")

    return query_id