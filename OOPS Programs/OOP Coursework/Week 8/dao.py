import csv   # functioanlity to erite to a CSV File #

def write_task_data_to_csv(task_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Title', 'Date Created', 'Due Date', 'Completed', 'Description', 'Priority']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for task in task_list.tasks:
            writer.writerow({
                'Title': task.title,
                'Date Created': task.date_created,
                'Due Date': task.date_due,
                'Completed': task.completed,
                'Description': task.description,
                'Priority': getattr(task, 'priority', '') 
            })
