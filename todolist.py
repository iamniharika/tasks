import tkinter as tk
from tkinter import ttk
def add():
    task = addtask.get()
    if task:
        tasktodo.insert(tk.END, task)
        addtask.delete(0, tk.END)
def remove():
    chosen = tasktodo.curselection()
    if chosen:
        tasktodo.delete(chosen)
frame = tk.Tk()
frame.title("***To-Do List***")
addtask = ttk.Entry(frame)
addtask.pack(pady=10)
add = ttk.Button(frame, text="Add", command=add)
add.pack(pady=10)
tasktodo = tk.Listbox(frame, selectmode=tk.MULTIPLE)
tasktodo.pack(pady=10)
remove = ttk.Button(frame, text="Remove", command=remove)
remove.pack(pady=10)
frame.mainloop()
