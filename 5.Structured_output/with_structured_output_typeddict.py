from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()

#schema 
class Review(TypedDict):
    summary: str 
    sentiment: str

structured_model=model.with_structured_output(Review)

result=structured_model.invoke(""" The hardware is great,but the software feels bloated.
there are too many pre-instaled apps that I can't remove .Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)