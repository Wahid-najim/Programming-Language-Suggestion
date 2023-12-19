import tkinter as tk
from tkinter import messagebox

def choose_language():
    what = var.get()
    user_input = user_entry.get()
    if what == "game development":
        messagebox.showinfo("Language Suggestion", "C++ is your best option. You entered: " + user_input)
    elif what == "dsa":
        messagebox.showinfo("Language Suggestion", "You can choose C, C++, or Java. You entered: " + user_input)
    elif what == "cyber security":
        messagebox.showinfo("Language Suggestion", "Python and C are the best options. You entered: " + user_input)
    elif what == "web development":
        messagebox.showinfo("Language Suggestion", "You need to learn HTML, CSS, JS, JavaScript framework/Python framework for backend. You can also learn PHP/Java for backend. You entered: " + user_input)
    elif what == "app development":
        messagebox.showinfo("Language Suggestion", "Swift for iOS and Kotlin for Android. You entered: " + user_input)
    else: # ai/ml
        messagebox.showinfo("Language Suggestion", "Python is the best. You entered: " + user_input)

root = tk.Tk()
root.geometry('500x200')  # Set the width and height of the window
root.title('Language Suggestion App')  # Set the title of the window
root.configure(bg='light blue')  # Set the background color of the window

var = tk.StringVar()

choices = ["game development", "dsa", "cyber security", "web development", "app development", "ai/ml"]
var.set(choices[0])

option_menu = tk.OptionMenu(root, var, *choices)
option_menu.config(width=50, bg='white', fg='black')  # Set the width, background color, and text color of the dropdown menu
option_menu.pack()

user_entry = tk.Entry(root)
user_entry.pack()

button = tk.Button(root, text="Submit", command=choose_language)
button.config(bg='green', fg='white')  # Set the background color and text color of the button
button.pack()

root.mainloop()
