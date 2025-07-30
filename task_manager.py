class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, description):
        """Add a new task to the list"""
        task = {
            'id': self.next_id,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"✓ Added task: {description}")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks yet! Add some tasks to get started.")
            return
        
        print("\n--- Your Tasks ---")
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} {task['id']}. {task['description']}")
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"✓ Completed: {task['description']}")
                return
        print("Task not found!")

def main():
    tm = TaskManager()
    
    while True:
        print("\n=== Personal Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks") 
        print("3. Complete Task")
        print("4. Quit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            description = input("Enter task description: ").strip()
            if description:
                tm.add_task(description)
            else:
                print("Please enter a task description!")
        
        elif choice == '2':
            tm.view_tasks()
        
        elif choice == '3':
            tm.view_tasks()
            try:
                task_id = int(input("Enter task ID to complete: "))
                tm.complete_task(task_id)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '4':
            print("Thanks for using Task Manager! 👋")
            break
        
        else:
            print("Invalid choice! Please choose 1-4.")

if __name__ == "__main__":
    main()