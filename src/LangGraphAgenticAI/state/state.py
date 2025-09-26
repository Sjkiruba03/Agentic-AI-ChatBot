from typing_extensions import TypedDict, List
from typing import Annotated
from langgraph.graph.message import add_messages


class State(TypedDict):

    """
    This class is represent the strcuture of the graph
    """

    messages : Annotated[List, add_messages]