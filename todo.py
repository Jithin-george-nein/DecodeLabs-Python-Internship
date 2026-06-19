def main():
    my_tasks = []
    
    while True:
        print("\n--- TO-DO LIST ENGINE ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            task_text = input("Enter the task description: ").strip()
            if task_text:
                # Store as a dictionary simulating a database table row
                task_id = len(my_tasks) + 1
                new_task = {"id": task_id, "task": task_text}
                my_tasks.append(new_task)
                print(f"Task '{task_text}' added successfully with ID {task_id}!")
        
        elif choice == '2':
            if not my_tasks:
                print("Your to-do list is empty.")
            else:
                print("\nCurrent Tasks:")
                # Use standard enumerate for simultaneous index and value access
                for idx, task_item in enumerate(my_tasks):
                    print(f"[{idx + 1}] ID: {task_item['id']} | Task: {task_item['task']}")
        
        elif choice == '3':
            print("Exiting system backend. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()