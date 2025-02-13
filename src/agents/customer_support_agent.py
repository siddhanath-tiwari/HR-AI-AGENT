# from langchain.llms import OpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationalRetrievalChain
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma

# class CustomerSupportAgent:
#     def __init__(self):
#         self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#         self.llm = OpenAI(model_name="gpt-4")  # Replace with open-source LLM if needed
#         self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#         self.vector_db = Chroma(persist_directory="./data/hr_policies", embedding_function=self.embedding)
#         self.chain = ConversationalRetrievalChain.from_llm(self.llm, retriever=self.vector_db.as_retriever(), memory=self.memory)

#     def handle_query(self, query):
#         response = self.chain({"question": query})
#         return response["answer"]


from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI  # Open-source LLM ke liye yeh replace karna hoga

class CustomerSupportAgent:
    def __init__(self):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.llm = ChatOpenAI(model_name="gpt-4")  # Agar OpenAI API nahi chahiye toh HuggingFace model replace karo
        self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_db = Chroma(persist_directory="./data/hr_policies", embedding_function=self.embedding)

        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm, 
            retriever=self.vector_db.as_retriever(), 
            memory=self.memory
        )

    def handle_query(self, query):
        response = self.chain.invoke({"question": query})
        return response.get("answer", "Mujhe is prashna ka jawab nahi mila.")

