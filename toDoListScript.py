#This creates a simple
#Scritp to-do list
import sys
import time

#tasks = set()
tasks = []

#Functions
def add_task():
    try:
        user_no_tasks = int(input("How many tasks would you like to enter? "))

        for task in range(user_no_tasks):
            user_task = input("Enter Task: ")
            tasks.append(user_task)

    except ValueError:
        print("Please enter a valid number of tasks to add to your list. ")
        #time.sleep(2)


def display_task():

    if tasks:
        print("Your tasks: ")
        time.sleep(1)

        for i, task in enumerate(tasks):
            i += 1
            print(str(i)+"." + task)
    else:
        print("Your to do list is empty.")

def delete_task():

    display_task()
    delete_option = int(input("Choose a task to delete: "))

    if delete_option > 0 and delete_option <= len(tasks):
        del tasks[delete_option-1]
        time.sleep(1)
        display_task()

def exit_app():
    sys.exit()


while True:
    time.sleep(1)
    print("__________________________________________________________________________")
    print("Welcome to Daniel's "
          "To Do List")
    print("\npress \n1. To add a task"
          "\n2. to display tasks"
          "\n3. to delete a task"
          "\n4. to exit")

    print("______________________________________________________________________")
    try:
        user_choice = int(input(">> "))
        if user_choice == 1:
            add_task()
            print("\n")
            print("__________________________________________________________________")
            display_task()
            print("__________________________________________________________________")

        elif user_choice == 2:
            display_task()

        elif user_choice ==3:
            delete_task()

        elif user_choice == 4:
            exit_app()

    except ValueError:

        print("You messed up try again.")
