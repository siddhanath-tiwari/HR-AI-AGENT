from .query_agent import QueryAgent
from .followup_agent import FollowupAgent
from .interview_agent import InterviewAgent
from .resume_agent import ResumeAgent

# Initialize all agents dynamically
query_agent = QueryAgent()
followup_agent = FollowupAgent()
interview_agent = InterviewAgent()
resume_agent = ResumeAgent()