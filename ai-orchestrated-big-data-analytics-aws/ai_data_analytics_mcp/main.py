import json
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType

from glue_metadata import get_glue_metadata
from athena_tools import execute_query
from sql_generator import build_ctas_query
from config import PROMPT_SQL_PATH, OPEN_API_KEY


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPEN_API_KEY
)


def load_prompt(path: str, **kwargs):

    with open(path, "r") as f:
        template = f.read()

    return template.format(**kwargs)

@tool
def list_tables():

    """
    Return available tables and columns from the Glue Catalog.
    """

    tables = get_glue_metadata()

    return json.dumps(tables, indent=2)


@tool
def generate_sql(user_request: str):

    """
    Generate a SQL query for Athena based on user request.
    """

    tables = get_glue_metadata()

    prompt = load_prompt(
        PROMPT_SQL_PATH,
        tables=tables,
        user_request=user_request
    )

    response = llm.invoke(prompt)

    return response.content


@tool
def run_analytics(sql_query: str):

    """
    Run SQL query in Athena using CTAS and save result in GOLD layer.
    """

    dataset_name = "ai_generated_dataset"

    ctas = build_ctas_query(
        table_name="",
        sql_body=sql_query,
        dataset_name=dataset_name
    )

    query_id = execute_query(ctas)

    return f"Query executed. Dataset stored in GOLD layer. QueryId={query_id}"


tools = [
    list_tables,
    generate_sql,
    run_analytics
]


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)


def run_mcp():

    print("\nAI Data Analyst MCP\n")

    user_input = input("What analysis do you want?\n")

    result = agent.invoke(user_input)

    print("\nResult:")
    print(result)


if __name__ == "__main__":
    run_mcp()