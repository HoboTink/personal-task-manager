from task_manager import TaskManager

# Quick demo of our task manager
print("=== Task Manager Demo ===")

tm = TaskManager()

# Add some sample tasks
tm.add_task("Learn Python basics")
tm.add_task("Build a cool project")
tm.add_task("Practice coding daily")

# View all tasks
tm.view_tasks()

# Complete a task
print("\nCompleting task 2...")
tm.complete_task(2)

# View updated tasks
tm.view_tasks()

print("\n🎉 Demo complete! Try running 'python task_manager.py' for the interactive version!")