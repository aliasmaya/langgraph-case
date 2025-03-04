from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import add_messages

class GraphState(TypedDict):
  content: Annotated[list, add_messages]