from langchain.llms import OpenAI

llm = OpenAI(model_name="gpt-4")

def process_query(data: str):
    return llm(data)