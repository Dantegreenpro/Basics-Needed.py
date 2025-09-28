#!/usr/bin/env python3
"""
Todo List Application

A command-line todo list manager that demonstrates:
- File I/O operations
- Data persistence
- User interface design
- Error handling
- Object-oriented programming

Features:
- Add, remove, and mark tasks as complete
- Save tasks to file
- Load tasks from file
- Display tasks with status
- Task priority levels
"""

import json
import os
from datetime import datetime
from enum import Enum

class Priority(Enum):
    """Task priority levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    """Individual task representation"""
    
    def __init__(self, description, priority=Priority.MEDIUM):
        self.id = None  # Will be set by TodoList
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def mark_complete(self):
        """Mark task as completed"""
        self.completed = True
        self.completed_at = datetime.now().isoformat()
    
    def mark_incomplete(self):
        """Mark task as incomplete"""
        self.completed = False
        self.completed_at = None
    
    def to_dict(self):
        """Convert task to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'description': self.description,
            'priority': self.priority.value,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary"""
        task = cls(data['description'], Priority(data['priority']))
        task.id = data['id']
        task.completed = data['completed']
        task.created_at = data['created_at']
        task.completed_at = data['completed_at']
        return task
    
    def __str__(self):
        status = "✅" if self.completed else "❌"
        priority_symbols = {Priority.LOW: "🔵", Priority.MEDIUM: "🟡", Priority.HIGH: "🔴"}
        priority_symbol = priority_symbols[self.priority]
        
        return f"[{self.id}] {status} {priority_symbol} {self.description}"

class TodoList:
    """Todo list manager"""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, description, priority=Priority.MEDIUM):
        """Add a new task"""
        task = Task(description, priority)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return f"Added task: {task.description}"
    
    def remove_task(self, task_id):
        """Remove a task by ID"""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                removed_task = self.tasks.pop(i)
                self.save_tasks()
                return f"Removed task: {removed_task.description}"
        return f"Task {task_id} not found"
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task.id == task_id:
                if task.completed:
                    return f"Task {task_id} is already completed"
                task.mark_complete()
                self.save_tasks()
                return f"Completed task: {task.description}"
        return f"Task {task_id} not found"
    
    def uncomplete_task(self, task_id):
        """Mark a task as incomplete"""
        for task in self.tasks:
            if task.id == task_id:
                if not task.completed:
                    return f"Task {task_id} is already incomplete"
                task.mark_incomplete()
                self.save_tasks()
                return f"Marked incomplete: {task.description}"
        return f"Task {task_id} not found"
    
    def list_tasks(self, show_completed=True, filter_priority=None):
        """List all tasks with optional filtering"""
        if not self.tasks:
            return "No tasks found"
        
        filtered_tasks = self.tasks
        
        # Filter by completion status
        if not show_completed:
            filtered_tasks = [task for task in filtered_tasks if not task.completed]
        
        # Filter by priority
        if filter_priority:
            filtered_tasks = [task for task in filtered_tasks if task.priority == filter_priority]
        
        if not filtered_tasks:
            return "No tasks match the criteria"
        
        # Sort by priority (high to low) then by creation date
        filtered_tasks.sort(key=lambda t: (-t.priority.value, t.created_at))
        
        result = "Your Tasks:\n" + "=" * 50
        for task in filtered_tasks:
            result += f"\n{task}"
        
        return result
    
    def get_statistics(self):
        """Get task statistics"""
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task.completed])
        pending_tasks = total_tasks - completed_tasks
        
        priority_counts = {
            Priority.HIGH: len([t for t in self.tasks if t.priority == Priority.HIGH and not t.completed]),
            Priority.MEDIUM: len([t for t in self.tasks if t.priority == Priority.MEDIUM and not t.completed]),
            Priority.LOW: len([t for t in self.tasks if t.priority == Priority.LOW and not t.completed])
        }
        
        stats = f"""
Task Statistics:
================
Total tasks: {total_tasks}
Completed: {completed_tasks}
Pending: {pending_tasks}
Completion rate: {(completed_tasks/total_tasks*100) if total_tasks > 0 else 0:.1f}%

Pending by Priority:
🔴 High: {priority_counts[Priority.HIGH]}
🟡 Medium: {priority_counts[Priority.MEDIUM]}
🔵 Low: {priority_counts[Priority.LOW]}
"""
        return stats
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            data = {
                'tasks': [task.to_dict() for task in self.tasks],
                'next_id': self.next_id
            }
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                
                self.tasks = [Task.from_dict(task_data) for task_data in data['tasks']]
                self.next_id = data.get('next_id', 1)
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
            self.next_id = 1

class TodoApp:
    """Main application class"""
    
    def __init__(self):
        self.todo_list = TodoList()
        self.running = True
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("📝 TODO LIST MANAGER")
        print("="*50)
        print("1. Add task")
        print("2. List all tasks")
        print("3. List pending tasks")
        print("4. Complete task")
        print("5. Remove task")
        print("6. Mark task incomplete")
        print("7. Show statistics")
        print("8. Filter by priority")
        print("9. Exit")
        print("-"*50)
    
    def get_priority_input(self):
        """Get priority level from user"""
        print("Priority levels:")
        print("1. Low 🔵")
        print("2. Medium 🟡")
        print("3. High 🔴")
        
        while True:
            try:
                choice = int(input("Enter priority (1-3): "))
                if choice in [1, 2, 3]:
                    return Priority(choice)
                else:
                    print("Please enter 1, 2, or 3")
            except ValueError:
                print("Please enter a valid number")
    
    def run(self):
        """Main application loop"""
        print("Welcome to Todo List Manager! 🎯")
        
        # Demo mode - pre-populate with some tasks
        if not self.todo_list.tasks:
            print("Setting up demo tasks...")
            self.todo_list.add_task("Learn Python basics", Priority.HIGH)
            self.todo_list.add_task("Practice coding exercises", Priority.MEDIUM)
            self.todo_list.add_task("Read Python documentation", Priority.LOW)
            self.todo_list.add_task("Build a project", Priority.HIGH)
            self.todo_list.complete_task(1)  # Mark first task as complete
        
        while self.running:
            self.display_menu()
            
            try:
                choice = input("Enter your choice (1-9): ").strip()
                
                if choice == '1':
                    self.add_task()
                elif choice == '2':
                    self.list_all_tasks()
                elif choice == '3':
                    self.list_pending_tasks()
                elif choice == '4':
                    self.complete_task()
                elif choice == '5':
                    self.remove_task()
                elif choice == '6':
                    self.uncomplete_task()
                elif choice == '7':
                    self.show_statistics()
                elif choice == '8':
                    self.filter_by_priority()
                elif choice == '9':
                    self.exit_app()
                else:
                    print("Invalid choice. Please select 1-9.")
                
                if choice != '9':
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def add_task(self):
        """Add a new task"""
        description = input("Enter task description: ").strip()
        if not description:
            print("Task description cannot be empty!")
            return
        
        priority = self.get_priority_input()
        result = self.todo_list.add_task(description, priority)
        print(f"✅ {result}")
    
    def list_all_tasks(self):
        """List all tasks"""
        print(self.todo_list.list_tasks())
    
    def list_pending_tasks(self):
        """List only pending tasks"""
        print(self.todo_list.list_tasks(show_completed=False))
    
    def complete_task(self):
        """Mark a task as completed"""
        self.list_pending_tasks()
        try:
            task_id = int(input("Enter task ID to complete: "))
            result = self.todo_list.complete_task(task_id)
            print(f"✅ {result}")
        except ValueError:
            print("Please enter a valid task ID")
    
    def remove_task(self):
        """Remove a task"""
        self.list_all_tasks()
        try:
            task_id = int(input("Enter task ID to remove: "))
            result = self.todo_list.remove_task(task_id)
            print(f"🗑️ {result}")
        except ValueError:
            print("Please enter a valid task ID")
    
    def uncomplete_task(self):
        """Mark a completed task as incomplete"""
        completed_tasks = [task for task in self.todo_list.tasks if task.completed]
        if not completed_tasks:
            print("No completed tasks found!")
            return
        
        print("Completed tasks:")
        for task in completed_tasks:
            print(f"  {task}")
        
        try:
            task_id = int(input("Enter task ID to mark incomplete: "))
            result = self.todo_list.uncomplete_task(task_id)
            print(f"↩️ {result}")
        except ValueError:
            print("Please enter a valid task ID")
    
    def show_statistics(self):
        """Show task statistics"""
        print(self.todo_list.get_statistics())
    
    def filter_by_priority(self):
        """Filter tasks by priority"""
        priority = self.get_priority_input()
        print(self.todo_list.list_tasks(filter_priority=priority))
    
    def exit_app(self):
        """Exit the application"""
        print("Thanks for using Todo List Manager! 👋")
        print("Your tasks have been saved automatically.")
        self.running = False

# Demo the application
if __name__ == "__main__":
    print("🚀 Todo List Application Demo")
    print("=" * 40)
    
    # Create a demo app and run a few operations
    app = TodoApp()
    
    # Show current state
    print("\nCurrent tasks:")
    print(app.todo_list.list_tasks())
    
    print("\nStatistics:")
    print(app.todo_list.get_statistics())
    
    print("\nPending tasks only:")
    print(app.todo_list.list_tasks(show_completed=False))
    
    print("\n" + "="*50)
    print("Demo completed! To run the interactive app, uncomment the line below:")
    print("# app.run()")
    print("="*50)
    
    # Uncomment this line to run the interactive application:
    # app.run()
    
    print("\n🎉 Todo List App project completed!")
    print("This project demonstrates:")
    print("✅ Object-oriented programming")
    print("✅ File I/O with JSON")
    print("✅ Error handling")
    print("✅ User interface design")
    print("✅ Data persistence")
    print("✅ Enums and datetime handling")