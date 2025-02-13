from src.agents.customer_support_agent import CustomerSupportAgent
from src.agents.recruitment_agent import RecruitmentAgent

if __name__ == "__main__":
    support_agent = CustomerSupportAgent()
    recruit_agent = RecruitmentAgent()

    print("Customer Support Test:")
    print(support_agent.handle_query("What is the leave policy?"))

    print("\nRecruitment Agent Test:")
    print(recruit_agent.generate_job_description("Software Engineer"))