tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")

def view_tasks():
    if tasks:
        print("To-do list:")
        for task in tasks:
            print("- " + task)
    else:
        print("Your to-do list is empty.")

while True:
    print("Welcome to your to-do list!")
    print("1.Krishala, Add a task")
    print("2. Krishala,Remove a task")
    print("3. You can View your tasks")
    print("4. Krishala,Exit")

    choice = int(input("Enter your choice Sanu : "))

    if choice == 1:
        task = input("Enter the task sanu: ")
        add_task(task)
    elif choice == 2:
        task = input("Enter the task to remove sanu: ")
        remove_task(task)
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        print("Sanu,Thank you for using the to-do list!")
        break
    else:
        print("Invalid choice. Please try again hus.")
