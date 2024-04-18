from tasks import Task
import datetime
from users import Owner

class TaskList:
    def __init__(self, owner: Owner): # added type as Owner
        
        self.owner = owner
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        del self.tasks[ix]

    def view_tasks(self) -> None:
        print(f"Task list for {self.owner}:")
        for ix, task in enumerate(self.tasks):
            print(f"{ix}: {task}")
    
    def view_overdue_tasks(self) -> None:
        current_date = datetime.datetime.now()
        print("Overdue tasks:")
        for task in self.tasks:
            if Task.date_due < current_date and not task.completed:
                print(task)

