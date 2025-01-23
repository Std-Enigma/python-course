"""
# Capstone Project: Python Mini Project

## Project Idea:
- Build a simple task management application where users can add, delete, and view tasks.

## Features:
1. Add tasks
2. View all tasks
3. Delete tasks
4. Mark tasks as complete

## Technologies Used:
- Python
- JSON for data storage
- Tkinter for GUI

## Next Steps:
- Start coding the project using the learned concepts.
"""

# Session 30 - Task Manager Application

import json
import tkinter as tk


class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def get_tasks(self):
        return self.tasks


# GUI Application
def add_task():
    task = task_entry.get()
    task_manager.add_task(task)
    task_entry.delete(0, tk.END)
    update_task_list()


def update_task_list():
    tasks = task_manager.get_tasks()
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task["task"])


task_manager = TaskManager()

# Create the main window
root = tk.Tk()
root.title("Task Manager")

# Create and place widgets
task_label = tk.Label(root, text="Enter a task:")
task_label.pack()

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(root)
task_list.pack()

# Load existing tasks
update_task_list()

# Run the application
root.mainloop()
