from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5")

result = llm.invoke("What is the capital of India?")

print(result.content)