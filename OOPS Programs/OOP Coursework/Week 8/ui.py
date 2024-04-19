from tasklist import TaskList
from tasks import Task
import datetime
from users import Owner
from prioritytask import PriorityTask
from dao import write_task_data_to_csv
from controllers import get_overdue_tasks



def main() -> None:
    # creating a new task list object
    task_list = TaskList("YOUR NAME")
    owner_name = input("Enter your name: ")
    owner = Owner(owner_name)
    task_list = TaskList(owner)  # saving a dfault task list with the owner class


    while True: 
        print("To-Do List Manager") 
        print("1. Add a task") 
        print("2. View tasks") 
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Complete a task")
        print("6. Export to file")
        print("7. View overdue tasks")
        print("8. Quit")
            
        choice = input("Enter your choice: ") 
            
        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            description1 = input("Enter a Description:")   # added functionlaity to get description
            priority = int(input("Enter priority (1 for low, 2 for medium, 3 for high): "))
            task = PriorityTask(title, date_object, priority, description1)
            task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()
           

        elif choice == "3":
            ix = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
    
        elif choice == "4":
            ix = int(input("Enter the index of the task to edit: "))
            choice = input("What would you like to edit? (title/due date/priority/description): ")

            if choice == "title":
                title = input("Enter a new title: ")
                task_list.tasks[ix].change_title(title)
                print("title changed successfully")
            elif choice == "due date":
                input_date = input("Enter a new due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task_list.tasks[ix].change_date_due(date_object)
                print("due date changed successfully")
            elif choice == "description":   # added functionality to change description
                title = input("Enter a new description: ")
                task_list.tasks[ix].change_description(title)
                print("desription changed successfully")
            elif choice == "priority":
                priority = int(input("Enter a new priority (1 for low, 2 for medium, 3 for high): "))
                task_list.tasks[ix].set_priority(priority)
                print("Priority changed successfully")
            else:
                print("Invalid choice.")
        
        elif choice == "5":
            ix = int(input("Enter the index of the task to complete: "))
            task_list.tasks[ix].mark_completed()

        elif choice == "6":
            write_task_data_to_csv(task_list, 'task_data.csv')    # please check current working directry 
            print("please check current working directory for the CSV File")
    

        elif choice == "7":
            overdue_tasks = get_overdue_tasks(task_list)
            print("Overdue tasks:")
            for task in overdue_tasks:
                print(task)
        
        elif choice == "8":
            break



if __name__ == "__main__":
    main()

