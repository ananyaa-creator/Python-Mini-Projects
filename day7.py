import os

TASK_FILE = "tasks.txt"
def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                text,status = line.strip().rstrip("||",1)
                tasks.append({"text":text,"done":status == "done"})
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE,"w",encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else ["not done"]
            f.write(f"{task['text']}||{status}\n")


def display_task(tasks):
    if not tasks:
        print("no tasks found")
    else:
        for i,task in enumerate(tasks,1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()

def task_manager():
    tasks = load_tasks()
    while True:
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()
        match choice:
            case "1":
                text = input("Enter your task").strip()
                if text:
                    tasks.append({"text":text, "done": False})
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty")
            case "2":
                display_task(tasks)
            case "3":
                display_task(tasks)
                try:
                    num = int(input("enter task number: "))
                    if 1<= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as done")
                    else:
                        print("invalid task number")
                except ValueError:
                    print("Please enter a number: ")
            case "4":
                display_task(tasks)
                try:
                    num = int(input("enter task number: "))
                    if 1<= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        save_tasks(tasks)
                        print(f"task removed {removed['text']}")
                    else:
                        print("invalid task number")
                except ValueError:
                    print("Please enter a number: ")
            case "5":
                print("Exiting task manager")
                break
            case _:
                print("please choose a valid option")

task_manager()
