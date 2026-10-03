from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=300)

documents=[
    "Virat kohli is the greatest player in the world",
    "Rohit sharma is the captain of Mumbai Indians",
    "M.S.Dhoni is one of the best captain india has ever seen ",
    "ABD is known as 360 player",
    "RCB  has the most crazy fandom"
]

query="tell me about rcb"

docs_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=(cosine_similarity([query_embedding], docs_embeddings))[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score:",score)
