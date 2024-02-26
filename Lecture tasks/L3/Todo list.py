
## defining functions
# adding a task

def add_task(taskaddstring):
    list_init.append(taskaddstring)

# Viewing a task
def view_task():
    print("----------------")
    for i, tasks in enumerate(list_init):
        print(i+1, tasks)
    print("----------------")

# Removing a Task
def remove_task():
    print("----------------")
    for i, tasks in enumerate(list_init):
        print(i+1, tasks)
    print("----------------")  
    rem1 = int(input("please select which task you want to remove from the list"))
    rem_calc = rem1 - 1
    list_init.pop(rem_calc)
    print("----------------")
    for i, tasks in enumerate(list_init):
        print(i+1, tasks)
    print("----------------")  


# Exiting a program
def exit_program():
    print("thank you for using the program, Program exited")
    quit()

# Gettting an Input from the user    
def input_option():
    print("#####   TO-DO LIST   ######")
    print("1. Add a new task\n2. View the current tasks in the list\n3. Remove a task from the list\n4. Quit and exit the program ")
    input1 = int(input("please select an option to proceed\n"))
    return input1

# Main Loop Function
def loop_function():
    get_input = input_option()
    while get_input < 6:

        if get_input == 1:
            new_task = str(input("please enter a new task\n"))
            add_task(new_task)
            loop_function()
            break

        elif get_input == 2:
            view_task()
            loop_function()
            break
                    
        elif get_input == 3:
            remove_task()
            loop_function()
            break

        elif get_input ==4:
            quit()

        else:
            print("\nplease select a valid selection")
            break

# Main Program

list_init = []
loop_function()
print("Thank you for using the program")

    
