"""Data Access"""
import json
import os


class TaskStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self._load_tasks()

    def _load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def _save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self._save_tasks()

    def get_tasks(self):
        return self.tasks

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self._save_tasks()
            return True
        return False
