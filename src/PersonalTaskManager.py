#!/usr/bin/env python
# coding: utf-8

# In[7]:


#import
import tkinter as tk
from tkinter import messagebox


# In[8]:


#Interface making
class MyGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Task Manager")
        self.root.geometry("600x400")
        self.root.resizable(0, 0)
        self.tasks=[]

        self.header_label = tk.Label(root, text = "Personal Task Manager",font = ("Helvetica", "12","bold"))    
        self.header_label.place(x = 200, y = 10)
        
        self.task_label = tk.Label(root,text = "Enter the Task:",font = ("Arial", "11" ))    
        self.task_label.place(x = 30, y = 40)
   
        self.task_entry = tk.Entry(root, width=30, font=('Arial', 11))
        self.task_entry.place(x = 30, y = 60)
        
        add_button = tk.Button(root, text="Add Task", command=self.add_task, font=('Arial', 10)) 
        add_button.place(x = 300, y = 58)

        self.task_listbox = tk.Listbox(root, width=30, height=10, font=('Arial', 11)) 
        self.task_listbox.place(x = 30, y = 100)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=('Arial', 10)) 
        self.remove_button.place(x = 30, y = 300)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, font=('Arial', 10)) 
        self.complete_button.place(x = 150, y = 300)

        self.task_listbox.bind('<Double-Button-1>', lambda event: self.complete_task())
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
                

    def remove_task(self):  
        the_value = self.task_listbox.curselection() 
        if the_value:  
            self.tasks.pop(the_value[0])
            self.update_task_list()
        else:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')
            
        
    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            completed_task = self.tasks.pop(selected_task_index[0])
            completed_task = f"[Done] {completed_task}"
            self.tasks.append(completed_task)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "No task selected.")
                
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def close(self):  
        print(self.tasks)  
        app.destroy()
    
    def clear_list(self):  
        self.task_listbox.delete(0, 'end')  

    
            

        


# In[9]:


if __name__ == "__main__":
    root = tk.Tk()
    app = MyGui(root) 
    root.mainloop()
    


# In[ ]:





# In[ ]:




