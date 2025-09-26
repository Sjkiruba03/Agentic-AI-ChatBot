from langchain.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode, tools_condition


def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools = [TavilySearchResults(max_results= 2)]
    print("tavily is called ")
    return tools


def create_tool_node(tools):
    """
    Create and return tool node for the Graph
    """
    return ToolNode(tools=tools)


