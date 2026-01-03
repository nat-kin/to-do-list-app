import json
import os

TODO_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a number!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            del tasks[num]
            print("Task deleted!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a number!")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Done")
        print("4. Delete Task")
        print("5. Quit & Save")
        choice = input("Choose: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved! Bye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
