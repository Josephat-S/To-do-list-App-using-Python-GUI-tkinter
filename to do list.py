import tkinter as tk
from tkinter import messagebox
# Create a class for the To-Do List app
class ToDoApp:
# Create a constructor that initializes the root window and the tasks list
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Create and place widgets
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)
# Create methods to add tasks
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
#  Create methods to remove tasks
    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")
# Create a method to clear all tasks
    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.clear()
        messagebox.showinfo("Clear", "All tasks have been cleared.")
#   Create a main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

#   End of program