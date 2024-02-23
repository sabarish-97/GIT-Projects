list_init = [""]
print("1. Add a new task\n2. View the current tasks in the list\n3. Remove a task from the list\n4. Quit and exit the program ")
def add_task(taskaddstring):
    list_init.append(taskaddstring)

def view_task():
    print(f"{list_init}")

def remove_task():
    print(f"please select which task you want to remove from the list{list_init}")
    rem1 = int(input)
    list_init.pop(rem1)
    print(f"The updated list is as follows {list_init}")

def exit_program():
    print("thank you for using the program, Program exited")
    quit()

get_input = int(input("please select an option to proceed"))

if get_input == 1:
    new_task = str(input("please enter a new task"))
    add_task(new_task)

elif get_input == 2:
    view_task()

elif get_input == 3:
    remove_task()

elif get_input == 4:
    exit_program()

else:
    print("\nplease select a valid selection")


    
