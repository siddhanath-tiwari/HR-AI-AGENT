# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate

# class RecruitmentAgent:
#     def __init__(self):
#         self.llm = OpenAI(model_name="gpt-4")
#         self.prompt = PromptTemplate(input_variables=["job_role"], template="Generate a job description for {job_role}")
#         self.jd_chain = LLMChain(llm=self.llm, prompt=self.prompt)

#     def generate_job_description(self, role):
#         return self.jd_chain.run(role)


from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class RecruitmentAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4")  # Open-source LLM ke liye replace karna hoga
        self.prompt = PromptTemplate(
            input_variables=["job_role"],
            template="Generate a detailed job description for the role of {job_role}."
        )
        self.jd_chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_job_description(self, role):
        response = self.jd_chain.invoke({"job_role": role})
        return response.get("text", "Job description generate nahi ho payi.")
