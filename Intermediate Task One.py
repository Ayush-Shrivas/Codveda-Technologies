Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import json
... import os
... 
... # File to store tasks
... FILE_NAME = "tasks.json"
... 
... # Load tasks from file
... def load_tasks():
...     if os.path.exists(FILE_NAME):
...         with open(FILE_NAME, 'r') as file:
...             return json.load(file)
...     return []
... 
... # Save tasks to file
... def save_tasks(tasks):
...     with open(FILE_NAME, 'w') as file:
...         json.dump(tasks, file, indent=4)
... 
... # Add task
... def add_task(task):
...     tasks = load_tasks()
...     tasks.append({"task": task, "done": False})
...     save_tasks(tasks)
...     print("Task added.")
... 
... # View tasks
... def view_tasks():
...     tasks = load_tasks()
...     if not tasks:
...         print("No tasks found.")
...     else:
...         for i, t in enumerate(tasks, start=1):
...             status = "✅" if t["done"] else "❌"
...             print(f"{i}. {t['task']} [{status}]")
... 
... # Mark task as done
... def mark_done(index):
...     tasks = load_tasks()
...     try:
...         tasks[index - 1]["done"] = True
...         save_tasks(tasks)
...         print("Task marked as done.")
...     except IndexError:
...         print("Error: Task not found.")
... 
# Delete task
def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    except IndexError:
        print("Error: Task not found.")

# Main menu
def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                num = int(input("Enter task number to mark as done: "))
                mark_done(num)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            view_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
