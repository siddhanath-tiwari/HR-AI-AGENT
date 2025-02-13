from fastapi import APIRouter
from agents.query_agent import QueryAgent

router = APIRouter()
query_agent = QueryAgent()

@router.post("/hr-query")
def hr_query(query: str):
    return {"response": query_agent.handle_query(query)}