
def add_task(taskaddstring):
    list_init.append(taskaddstring)
    
def view_task():
    print(f"{list_init}")
    

def remove_task():
    print(f"this is the list{list_init}")
    rem1 = int(input("please select which task you want to remove from the list"))
    rem_calc = rem1 - 1
    list_init.pop(rem_calc)
    print(f"The updated list is as follows {list_init}")

def exit_program():
    print("thank you for using the program, Program exited")
    quit()
    
def input_option():
    print("1. Add a new task\n2. View the current tasks in the list\n3. Remove a task from the list\n4. Quit and exit the program ")
    input1 = int(input("please select an option to proceed\n"))
    return input1

def loop_function():
    get_input = input_option()
    while get_input < 5:

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

        else:
            print("\nplease select a valid selection")
            break

list_init = []
loop_function()

    
