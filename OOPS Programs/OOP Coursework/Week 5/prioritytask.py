# prioritytask.py

class PriorityTask:
    PRIORITY_MAP = {1: 'low', 2: 'medium', 3: 'high'}

    def __init__(self, title: str, priority: int, description: str):
        self.title = title
        self.description = description
        self.set_priority(priority)

    def set_priority(self, priority: int) -> None:
        if priority not in self.PRIORITY_MAP:
            raise ValueError("Priority level must be between 1 and 3")
        self.priority = priority

    def get_priority_str(self) -> str:
        return self.PRIORITY_MAP[self.priority]

    def __str__(self) -> str:
        return f"Title: {self.title}, Description: {self.description}, Priority: {self.get_priority_str()}"

# You can include any additional related code here, such as functions or constants.
