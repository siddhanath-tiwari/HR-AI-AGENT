from services.schedule import  Scheduled_followup

class FollowupAgent:
    def create_followup(self, employee_id, task):
        return Scheduled_followup(employee_id, task)
        