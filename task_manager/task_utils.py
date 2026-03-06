from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task():
    title = input("Enter task title: ")
    if not validate_task_title(title):
        return

    description = input("Enter task description: ")
    if not validate_task_description(description):
        return

    due_date = input("Enter due date (YYYY-MM-DD): ")
    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['title']} - Completed: {task['completed']}")

    try:
        choice = int(input("Select task number to mark complete: "))
        tasks[choice - 1]["completed"] = True
        print("Task marked as complete!")
    except (ValueError, IndexError):
        print("Invalid task number.")


def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    for task in pending:
        print(f"{task['title']} - Due: {task['due_date']}")

def calculate_progress(tasks):
    completed = sum(1 for task in tasks if task["completed"])
    progress = (completed / len(tasks)) * 100
    return progress