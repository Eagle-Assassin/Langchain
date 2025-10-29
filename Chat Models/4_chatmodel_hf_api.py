from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint  #for using the API of hugging fae
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

result =model.invoke("What is the capital of India")

print(result.content)


