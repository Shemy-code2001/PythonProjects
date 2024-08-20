# TO-DO LIST:
tasks = ["task1", "task2"]

def AddTask(tasks):
    num = int(input("Enter the number of tasks to add: "))
    for i in range(num):
        task = input("Enter the new task: ")
        tasks.append(task)

def DeleteTask(tasks, name):
    if name in tasks:
        tasks.remove(name)

def ShowTasks(tasks):
    print("The tasks are:")
    for task in tasks:
        print(task)

def SaveTasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("The tasks in the list are:\n")
        for task in tasks:
            f.write(f"{task}\n")

SaveTasks(tasks)

# Main Program
while True:
    choice = input("""------------------MENU-----------------
1- Add tasks to the list.
2- Delete a task from the list.
3- Display the tasks.
4- Exit
Enter your choice: """)
    
    if choice == "1":
        AddTask(tasks)
        print("The tasks have been successfully added!")
    elif choice == "2":
        name = input("Enter the task you want to delete: ")
        DeleteTask(tasks, name)
    elif choice == "3":
        ShowTasks(tasks)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
