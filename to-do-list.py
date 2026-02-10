tasks = []
print("Welcome to the To-Do List App!")
while True:
    print("\nPlease choose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print(f"Task '{task}' added to the list.")
    elif choice == '2':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
    elif choice == '3':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            try:
                task_num = int(input("Enter the number of the task you want to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed from the list.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        
