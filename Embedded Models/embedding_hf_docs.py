from langchain_huggingface import HuggingFaceEmbeddings

embeddings =HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs =[
    "Delhi is the capital of India",
    "Kolkota is the capital of West Bengal",
    "paris is the capital of France"
]

result=embeddings.embed_documents(docs)

print(str(result))