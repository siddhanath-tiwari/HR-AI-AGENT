from services.db_service import get_hr_policy
from services.llm_service import process_query

class QueryAgent:
    def handle_query(self, query: str):
        data = get_hr_policy(query)
        response = process_query(data)
        return response