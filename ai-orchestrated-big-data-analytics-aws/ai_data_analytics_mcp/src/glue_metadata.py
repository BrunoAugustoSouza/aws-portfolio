from src.aws_clients import get_glue_client
from src.config import DATABASE_NAME

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
            "table": table["Name"],
            "columns": columns
        })

    return tables