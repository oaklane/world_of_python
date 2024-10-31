import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

def display_tasks(tasks):
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        command = input("Enter 'add' to add a task, 'list' to view tasks, or 'exit': ").strip().lower()
        if command == "add":
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif command == "list":
            display_tasks(tasks)
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")
