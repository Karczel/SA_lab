"""User interface"""
from data_access import TaskStorage
from business_logic import TaskManager


def main():
    storage = TaskStorage()
    manager = TaskManager(storage)

    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.print_tasks()

        elif choice == "2":
            title = input("Enter task title: ")
            manager.add_task(title)
            print("Task added.")

        elif choice == "3":
            manager.print_tasks()
            index = int(input("Enter task number to complete: "))-1
            if manager.complete_task(index):
                print("Task marked as complete.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            manager.print_tasks()
            index = int(input("Enter task number to delete: "))-1
            if manager.delete_task(index):
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


