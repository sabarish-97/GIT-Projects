from tasklist import TaskList
from tasks import Task
import datetime
from users import Owner
from prioritytask import PriorityTask

def propagate_task_list(task_list: TaskList) -> TaskList:
    
        #adding arguments to new parameter description
    
    task_list.add_task(PriorityTask("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4),2,"Restock Vegetables"))
    #task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4),"Restock Vegetables"))
    #task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2),"Wash white clothes"))
    #task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1),"Clean store room"))
    #task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3),"Do OOP Homework"))
    #task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5),"Take the pug"))
    #task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6),"Only the white plates"))
    #task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6),"jj"))



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
            break

        elif choice == "7":
            task_list.view_overdue_tasks()



if __name__ == "__main__":
    main()

