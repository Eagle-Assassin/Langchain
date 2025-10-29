from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

docs =[
    "Delhi is the capital of India",
    "Kolkota is the capital of West Bengal",
    "paris is the capital of France"
]

# result=embedding.embed_query("Delhi is the capital of India")
result=embedding.embed_documents(docs)

print(str(result))