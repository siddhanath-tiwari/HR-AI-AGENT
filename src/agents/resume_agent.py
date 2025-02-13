from services.llm_service import rank_candidates

class ResumeAgent:
    def screen_resume(self, resumes):
        return rank_candidates(resumes)