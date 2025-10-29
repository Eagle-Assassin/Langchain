from langchain_huggingface import ChatHuggingFace ,HuggingFacePipeline
import os

# os.environ["HF_HOME"] ="{path}" #to download the model to a specific path

llm =HuggingFacePipeline.from_model_id(    
    model_id="Qwen/Qwen3-4B-Instruct-2507",
    task="text-generation",pipeline_kwargs=dict(temperature=0.5,max_new_tokens=100))

model=ChatHuggingFace(llm=llm)

result=model.invoke("what is the capital of India")

print(result.content)
