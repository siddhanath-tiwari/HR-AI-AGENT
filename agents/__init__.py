from .query_agent import QueryAgent
from .folloowup_agent import FollowupAgent
from .interview_agent import InterviewAgent
from .resume_agent import ResumeAgent


# initialize all agents dynamically

query_agent = QueryAgent()
folloowup_agent = FollowupAgent()
interview_agent = InterviewAgent()
resume_agent = ResumeAgent()
