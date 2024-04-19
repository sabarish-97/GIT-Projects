import datetime

def get_overdue_tasks(task_list):
    current_date = datetime.datetime.now()     # Functionality to check for overdue tasks #
    overdue_tasks = []
    for task in task_list.tasks:
        if task.date_due < current_date and not task.completed:
            overdue_tasks.append(task)
    return overdue_tasks
