import datetime

class Task:
    

    def __init__(self, title: str, date_due: datetime.datetime,description):  # added description as parameter
        
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due
        self.description = description         # added description to as attribute

    def change_title(self, new_title: str) -> None:
        
        self.title = new_title

    def change_description(self, new_description):
        self.description = new_description

    def change_date_due(self, date_due: datetime.datetime) -> None:
        
        self.date_due = date_due

    def mark_completed(self) -> None:
        

        self.completed = True

    def __str__(self) -> str:
        return f"{self.title}, created: {self.date_created}, due: {self.date_due}, completed: {self.completed} description : {self.description})"  #added functionality to display description
    
class RecurringTask(Task):
    """Represents a recurring task in a to-do list.

    Args:
        Task (Task): The task to be repeated.
    """

    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        """Creates a new recurring task.

        Args:
            title (str): Title of the task.
            date_due (datetime.datetime): Due date of the task.
            interval (datetime.timedelta): Interval between each repetition.
        """
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates : list[datetime.datetime] = [] # type hinting that completed_dates is a list of datetime.datetime objects
    
    def _compute_next_due_date(self) -> datetime.datetime:
        """Computes the next due date of the task.

        Returns:
            datetime.datetime: The next due date of the task.
        """
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()
    
    def __str__(self) -> str:
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed: {self.completed_dates}, interval: {self.interval})"



class TaskFactory:
    @staticmethod
    def create_task(title:str, date:datetime.datetime, **kwargs:Any) -> Task:
        if "interval" in kwargs:
            return RecurringTask(title, date, kwargs["interval"])
        else:
            return Task(title, date)