import datetime
from typing import Any
from abc import ABC, abstractmethod

class Task:
    

    def __init__(self, title: str, date_due: datetime.datetime, description):  # added description as parameter
        
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
        return f"{self.title}, created: {self.date_created}, due: {self.date_due}, completed: {self.completed}. descripton : {self.description})"  #added functionality to display description
    
