from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4.1',temperature=0,max_completion_tokens=10) #temp (0-2) controls the randomness of a language model result, make how creative the LLm output is 

result=model.invoke("Write 5 line poem on cricket")

print(result.content)

