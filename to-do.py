tasks = []


def add():    
    job = input("Enter the task you would like to add to the list: ").upper()
    tasks.append(job)
    print(f"{job} has been added to the To Do List.")


def view():
    if tasks == []:
        print("There are currently no tasks in the To Do List.")
    else: 
        print("\nVIEWING TO-DO LIST:\n")
        for item in tasks:
            print(f"-{item}")


def delete():
    try:
        if tasks == []:
            print("There are no tasks in the list to delete.")
        else:
            print("\nTO-DO LIST:\n")
            for item in tasks:
                print(item)
            deleted_task = input("Type out the name of the task you would like to delete. ").upper()
            tasks.remove(deleted_task)
            print(f"{deleted_task} has been deleted.")  

    except ValueError:
        print("Please enter the exact name of the task you would like to delete.")



print("\nWelcome to the To-Do List App!")

while True:  
    print("\nMenu:\n")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

    try:
        choice = int(input("\nPlease enter the number of the action you would like to perform: "))
        if choice == 1: 
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            delete()
        elif choice == 4:
            break
        
    except ValueError:
        print("Please be sure to enter the number of the action.")

print("Thank you for using the to do list app!")
