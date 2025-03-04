from langgraph.graph import StateGraph
from state import GraphState
from nodes import generate
from constants import NODE_GENERATE, NODE_TOOL
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

graph_builder = StateGraph(GraphState)
graph_builder.add_node(NODE_GENERATE, generate)
# graph_builder.add_node(NODE_TOOL, ToolNode)
# graph_builder.add_conditional_edges(NODE_GENERATE, tools_condition)
# graph_builder.add_edge(NODE_TOOL, NODE_GENERATE)
graph_builder.set_entry_point(NODE_GENERATE)
app = graph_builder.compile(checkpointer=MemorySaver())