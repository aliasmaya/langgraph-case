import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatbot = ChatOpenAI(temperature=0, model=os.getenv('MODEL', ''))