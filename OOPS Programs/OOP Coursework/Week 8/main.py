from tasklist import TaskList
from tasks import Task
import datetime
from users import Owner

def propagate_task_list(task_list: TaskList) -> TaskList:
    
        #adding arguments to new parameter description
    
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4),"Restock Vegetables"))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2),"Wash white clothes"))
    task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1),"Clean store room"))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3),"Do OOP Homework"))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5),"Take the pug"))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6),"Only the white plates"))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6),"jj"))



    return task_list



def main() -> None:
    # creating a new task list object
    task_list = TaskList("YOUR NAME")

    # propagate the task list with some sample tasks
    task_list = propagate_task_list(task_list)

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
        print("6. Quit")
        print("7. View overdue tasks")
            
        choice = input("Enter your choice: ") 
            
        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            # create a new task object based on the title entered and the date entered
            description1 = input("Enter a Description:")   # added functionlaity to get description
            task = Task(title, date_object, description1)
            task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()
           

        elif choice == "3":
            ix = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
    
        elif choice == "4":
            ix = int(input("Enter the index of the task to edit: "))
            choice = input("What would you like to edit? (title/due date/description): ")

            if choice == "title":
                title = input("Enter a new title: ")
                task_list.tasks[ix].change_title(title)
            elif choice == "due date":
                input_date = input("Enter a new due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task_list.tasks[ix].change_date_due(date_object)
            if choice == "description":   # added functionality to change description
                title = input("Enter a new description: ")
                task_list.tasks[ix].change_description(title)
            else:
                print("Invalid choice.")
        
        elif choice == "5":
            ix = int(input("Enter the index of the task to complete: "))
            task_list.tasks[ix].mark_completed()

        elif choice == "6":
            break

        elif choice == "7":
            task_list.view_overdue_tasks()



if __name__ == "__main__":
    main()

