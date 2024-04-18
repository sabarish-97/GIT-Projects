from tasks import Task
import datetime

class PriorityTask(Task):
    PRIORITY_MAPPING = {1: 'low', 2: 'medium', 3: 'high'}

    def __init__(self, title: str, date_due: datetime.datetime, priority: int, description: str):
        super().__init__(title, date_due, description)
        self.set_priority(priority)

    def set_priority(self, priority: int) -> None:
        if priority < 1:
            self.priority = 1
        elif priority > 3:
            self.priority = 3
        else:
            self.priority = priority

    def __str__(self) -> str:
        priority_str = self.PRIORITY_MAPPING.get(self.priority, 'unknown')
        return f"{super().__str__()}, priority: {priority_str}"
