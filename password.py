import tkinter as tk
from tkinter import ttk
import random 
import string
def generatepassword():
        List = ""
        List += string.ascii_letters
        List += string.digits 
        List += string.punctuation
        password = []
        length = int(entry.get())
        for i in range(length):
                randomchar = random.choice(List)
                password.append((randomchar))
        passwords = "".join(password)
        result.config(text=f"Generated Password: {passwords}")

frame = tk.Tk()
frame.title("*** PASSWORD GENERATOR ***")

label = ttk.Label(frame, text="Enter the length of password ")
label.pack(pady=10)
entry = ttk.Entry(frame)
entry.pack(pady=10)
button = tk.Button(frame, text='generate', command=generatepassword)
button.pack()
result = ttk.Label(frame, text="")
result.pack(pady=10)
frame.mainloop()