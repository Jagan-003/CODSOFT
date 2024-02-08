class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index)
            print(f"Task '{task}' removed successfully!")
        except IndexError:
            print("Invalid task index!")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty!")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            if todo_list.tasks:
                task_index = int(input("Enter task index to remove: ")) - 1
                todo_list.remove_task(task_index)
            else:
                print("Your To-Do List is empty!")
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
