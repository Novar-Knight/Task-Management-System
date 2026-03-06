from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def menu():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_as_complete()
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            calculate_progress()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    menu()