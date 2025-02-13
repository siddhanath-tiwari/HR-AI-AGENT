from services.db_service import git_hr_policy
from services.llm_services import process_query


class QueryAgent:
    def handle_query(self, query):
        data = get_hr_policy(query)
        response = process_query(data)
        return response
        