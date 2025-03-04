from chains.chain import chatbot
from state import GraphState

def generate(state: GraphState):
  content = state['content']
  result = chatbot.invoke(content)
  return {
    'content': [result]
  }