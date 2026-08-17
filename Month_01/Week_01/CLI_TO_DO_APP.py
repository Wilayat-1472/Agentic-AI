tasks=[]

def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as done ")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ").strip()

    if not task:
        print("Task name cannot be empty.")
        return
    for existing_task in tasks:
        if existing_task["task"].casefold() == task.casefold():
            print("That task already exists.")
            return

    description = input("Enter task description: ").strip()

    tasks.append({"task": task,"description": description,"done": False})

    print(f"Task '{task}' added successfully.")


def view_task():
    if not tasks:
        print("no task yet!")
        return
    print("\n Your Tasks: ")
    for index,task in enumerate(tasks, start=1):
        status="Done" if task["done"] else "Pending"
        print(f"{index}. {task['task']} — {task['description']} [{status}]")
       

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index=int(input("Enter the task number done: "))-1
        if 0<=index<len(tasks):
            tasks[index]["done"]=True
            print("Marked as Done")
        else:
            print("Invalid number")

    except ValueError:
        print("Please Enter a Valid Number")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index=int(input("Enter Task Number to delete: "))-1
        if 0<=index<len(tasks):
            removed=tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number")
    except ValueError:
            print("Please Enter a Valid Number")

while True:
    show_menu()
    choice=input(" Choose an option (1-5): ")

    if choice=='1':
        add_task()
    elif choice=='2':
        view_task()
    elif choice=='3':
        mark_done()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        print("Goodbye!")
        break
    else:
        print("Invalid Choice Try again!")
      





