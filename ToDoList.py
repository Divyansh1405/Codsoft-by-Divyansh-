tasks = {}

def create_task(task_id, task_details):
    tasks[task_id] = task_details
    print(f"Task '{task_details}' added with ID: {task_id}")

def update_task(task_id, new_details):
    if task_id in tasks:
        tasks[task_id] = new_details
        print(f"Task with ID {task_id} updated to '{new_details}'")
    else:
        print(f"Task with ID {task_id} not found")

def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task with ID {task_id} deleted")
    else:
        print(f"Task with ID {task_id} not found")

def list_tasks():
    if tasks:
        print("Current tasks:")
        for task_id, task_details in tasks.items():
            print(f"ID: {task_id} - {task_details}")
    else:
        print("No tasks found")

if __name__ == "__main__":
    while True:
        print(""" 
                What Can I do for you ??
                    1. Add Task
                    2. Update Task
                    3. Delete Task
                    4. List Tasks
                    5. Exit
              """)
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_id = input("Enter task ID: ")
            task_details = input("Enter task details: ")
            create_task(task_id, task_details)
        elif choice == '2':
            task_id = input("Enter task ID to update: ")
            new_details = input("Enter new task details: ")
            update_task(task_id, new_details)
        elif choice == '3':
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            print("Exit")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
