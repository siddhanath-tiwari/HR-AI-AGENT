from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class CustomerSupportAgent:
    def __init__(self):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.llm = OpenAI(model_name="gpt-4")  # Replace with open-source LLM if needed
        self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_db = Chroma(persist_directory="./data/hr_policies", embedding_function=self.embedding)
        self.chain = ConversationalRetrievalChain.from_llm(self.llm, retriever=self.vector_db.as_retriever(), memory=self.memory)

    def handle_query(self, query):
        response = self.chain({"question": query})
        return response["answer"]