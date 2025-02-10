"""Business Logic"""


class TaskManager:
    def __init__(self, storage):
        self.storage = storage

    def add_task(self, title):
        task = {"title": title, "completed": False}
        self.storage.add_task(task)

    def list_tasks(self):
        return self.storage.get_tasks()

    def complete_task(self, index):
        tasks = self.storage.get_tasks()
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            self.storage._save_tasks()
            return True
        return False

    def delete_task(self, index):
        return self.storage.remove_task(index)

    def print_tasks(self):
        tasks = self.list_tasks()
        for i, task in enumerate(tasks):
            status = "[✓]" if task["completed"] else "[ ]"
            print(f"{i+1}. {status} {task['title']}")
