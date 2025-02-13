from services.scheduler import schedule_followup

class FollowupAgent:
    def create_followup(self, employee_id, task):
        return schedule_followup(employee_id, task)