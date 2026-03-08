import json
from langchain_openai import ChatOpenAI
from src.utils import load_prompt
from src.config import PROMPT_SUGGEST_PATH, GOLD_PATH, DATABASE_NAME
from src.glue_metadata import get_glue_metadata

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def suggest_queries():

    tables = get_glue_metadata()

    prompt = load_prompt(
        PROMPT_SUGGEST_PATH,
        tables=tables,
        GOLD_PATH=GOLD_PATH,
        database=DATABASE_NAME
    )
    
    response = llm.invoke(prompt)
    
    return json.loads(response.content)