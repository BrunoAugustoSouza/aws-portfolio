from mcp.server.fastmcp import FastMCP
from tool_definitions import get_tools
from query_executor import run_query

mcp = FastMCP("NYC Taxi Analytics MCP")

@mcp.tool()
def query_nyc_taxi(sql: str) -> str:
    return run_query(sql)

if __name__ == "__main__":
    mcp.run()