from langgraph.graph import StateGraph, START, END
from state import GraphState
from nodes import generate
from constants import NODE_GENERATE

graph_builder = StateGraph(GraphState)
graph_builder.add_node(NODE_GENERATE, generate)
graph_builder.add_edge(START, NODE_GENERATE)
graph_builder.add_edge(NODE_GENERATE, END)
app = graph_builder.compile()