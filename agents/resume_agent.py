from services.llm_service import rank_condidates
class  RankCondidates:
    def screen_resume(self, resumes):
        return rank_condidates(resumes)
