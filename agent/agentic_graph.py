from typing_extensions import TypedDict, Annotated
from typing import Any
from langchain_core.messages import HumanMessage, AnyMessage, SystemMessage

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from operator import add

from utilities.models import instantiate_azure_chat_openai
from tools.list_of_tools import search_duckduckgo, search_wikipedia
from tools.generate_answer import generate_answer

class State(TypedDict):
    query_id: int # query_id
    query: str  # User's query
    answer: str  # Generated answer
    retrieved_context: Annotated[list, add]  # Combined context

def build_simple_agent_chain():

    # Build the graph
    builder = StateGraph(State)

    # Test interaction with memory
    # Thread ID for maintaining context

    # Add nodes
    builder.add_node("search_duckduckgo", search_duckduckgo)
    builder.add_node("search_wikipedia", search_wikipedia)
    builder.add_node("generate_answer", generate_answer)

    # Define edges
    builder.add_edge(START, "search_duckduckgo")
    builder.add_edge(START, "search_wikipedia")
    builder.add_edge("search_duckduckgo", "generate_answer")
    builder.add_edge("search_wikipedia", "generate_answer")
    builder.add_edge("generate_answer", END)

    memory = MemorySaver() 
    react_graph_memory = builder.compile(checkpointer=memory)

    return react_graph_memory