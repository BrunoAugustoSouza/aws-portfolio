from config import DATABASE_NAME, REGION
from aws_clients import get_glue_client

glue = get_glue_client()

def get_glue_metadata():

    response = glue.get_tables(DatabaseName=DATABASE_NAME)

    tables = []

    for table in response["TableList"]:

        columns = [
            col["Name"]
            for col in table["StorageDescriptor"]["Columns"]
        ]

        tables.append({
            "table_name": table["Name"],
            "columns": columns
        })

    return tables