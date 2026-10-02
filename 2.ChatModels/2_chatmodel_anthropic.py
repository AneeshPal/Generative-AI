from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model=ChatAnthropic(model="claude-3-5 sonnet-20241022")
result=model.invoke("who is know as goat of cricket")
print(result.content)
