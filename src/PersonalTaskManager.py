import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):

        #creates the GUI
        self.root = root
        self.root.title("Personal Task Manager")
        self.root.geometry("600x400")
        self.root.resizable(0, 0)
        self.tasks=[]

        #Task heading
        self.header_label = tk.Label(root, text = "Personal Task Manager",font = ("Helvetica", "12","bold"))    
        self.header_label.place(x = 200, y = 10)
        
        #Task label
        self.task_label = tk.Label(root,text = "Enter the Task:",font = ("Arial", "11" ))    
        self.task_label.place(x = 30, y = 40)
   
        self.task_entry = tk.Entry(root, width=30, font=('Arial', 11))
        self.task_entry.place(x = 30, y = 60)
        
        #add button
        add_button = tk.Button(root, text="Add Task", command=self.add_task, font=('Arial', 10)) 
        add_button.place(x = 300, y = 58)
        
        #Creates listbox
        self.task_listbox = tk.Listbox(root, width=30, height=10, font=('Arial', 11)) 
        self.task_listbox.place(x = 30, y = 100)
        
        #delete button
        self.remove_button = tk.Button(root, text="Remove Task", command=self.delete_task, font=('Arial', 10)) 
        self.remove_button.place(x = 30, y = 300)
        
        #complete button
        self.complete_button = tk.Button(root, text="Complete Task", command=self.mark_complete, font=('Arial', 10)) 
        self.complete_button.place(x = 150, y = 300)

        self.task_listbox.bind('<Double-Button-1>', lambda event: self.mark_complete())

    #Side Effect free functions

    ## add task function    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    ## delete task function
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    
    #Complete task function
    def mark_complete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} - Completed")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    

#main function
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root) 
    root.mainloop()
    





