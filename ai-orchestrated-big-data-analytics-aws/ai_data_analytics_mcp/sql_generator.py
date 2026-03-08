from config import GOLD_PATH

def build_ctas_query(table_name, sql_body, dataset_name):

    ctas_query = f"""
    CREATE TABLE {dataset_name}
    WITH (
        format='PARQUET',
        external_location='{GOLD_PATH}{dataset_name}/'
    )
    AS
    {sql_body}
    """

    return ctas_query