import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

tool = TavilySearchResults(max_results=5)
bot = ChatOpenAI(temperature=0, model=os.getenv('MODEL', ''))
# chatbot = bot.bind_tools([tool])
chatbot = bot