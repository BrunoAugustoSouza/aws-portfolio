import json
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from glue_metadata import get_glue_metadata
from athena_tools import execute_query
from sql_generator import build_ctas_query
from utils import load_prompt
from config import PROMPT_SQL_PATH

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


@tool
def list_tables() -> str:
    """Return Glue tables and columns."""

    tables = get_glue_metadata()

    return json.dumps(tables)


@tool
def generate_sql(user_request: str) -> str:
    """Generate SQL query for Athena."""

    tables = get_glue_metadata()

    prompt = load_prompt(
        PROMPT_SQL_PATH,
        tables=tables,
        user_request=user_request
    )

    response = llm.invoke(prompt)

    return response.content


@tool
def run_analytics(sql_query: str) -> str:
    """Execute CTAS query and store result in S3 Gold layer."""

    dataset_name = "ai_generated_dataset"

    ctas = build_ctas_query(
        sql_query,
        dataset_name
    )

    query_id = execute_query(ctas)

    return f"Query executed successfully. QueryId={query_id}"


tools = [
    list_tables,
    generate_sql,
    run_analytics
]


agent = create_react_agent(
    model=llm,
    tools=tools
)


def run():

    print("\nAI Data Analytics MCP\n")

    user_input = input("Ask your question:\n")

    result = agent.invoke(
        {
            "messages": [
                ("user", user_input)
            ]
        }
    )

    print(result)


if __name__ == "__main__":
    run()