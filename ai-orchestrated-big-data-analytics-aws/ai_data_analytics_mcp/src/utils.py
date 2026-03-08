import re

def load_prompt(path: str, **kwargs):

    with open(path, "r") as f:
        template = f.read()

    return template.format(**kwargs)

def extract_external_location(sql: str) -> str:
    """
    Extrai o valor de external_location de uma query CREATE TABLE AS (CTAS) no Athena.

    Args:
        sql (str): Query CTAS do Athena.

    Returns:
        str: Caminho do S3 definido em external_location, ou None se não encontrado.
    """
    # Regex para capturar o conteúdo entre external_location='...'
    match = re.search(r"external_location\s*=\s*'([^']+)'", sql, re.IGNORECASE)
    if match:
        return match.group(1)
    return None