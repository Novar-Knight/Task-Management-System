# Task-Management-System

## Overview

The **Task Management System** is a simple command-line application built with Python that allows users to manage their daily tasks and track progress. Users can add tasks, mark them as complete, view pending tasks, and monitor their overall completion progress.

This project demonstrates the use of Python modules, packages, functions, and input validation to build a structured and maintainable program.

---

## Features

* Add new tasks
* Mark tasks as complete
* View pending tasks
* Track task completion progress
* Input validation for task details
* Modular project structure

---

## Project Structure

```
Task-Management-System
│
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
│
└── task_manager
    ├── __init__.py
    ├── task_utils.py
    └── validation.py
```

---

## Task Structure

Each task is represented using a Python dictionary:

```
task = {
    "title": "Groceries",
    "description": "Shop at Market Basket for food",
    "due_date": "2024-06-26",
    "completed": True
}
```

---

## Modules

### validation.py

Contains functions that validate user input.

Functions:

* `validate_task_title`
* `validate_task_description`
* `validate_due_date`

---

### task_utils.py

Contains the main task management logic.

Functions:

* `add_task`
* `mark_task_as_complete`
* `view_pending_tasks`
* `calculate_progress`

---

### main.py

Provides the user interface through a menu-based command-line system. It allows users to interact with the task manager and perform different operations.

---

## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/Task-Management-System.git
```

2. Navigate to the project directory

```
cd Task-Management-System
```

3. Install dependencies using Pipenv

```
pipenv install
```

4. Activate the environment

```
pipenv shell
```

---

## Running the Program

Run the application using:

```
python3 main.py
```

You will see a menu allowing you to manage tasks.

---

## Example Menu

```
Task Management System
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. Track Progress
5. Exit
```

---

## Technologies Used

* Python
* Pipenv
* Command Line Interface (CLI)

---

## Author

Created as part of a Python programming assignment to demonstrate modular programming, package organization, and task management functionality.
