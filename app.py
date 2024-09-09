# 1. Introduce
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# ttk.Label(root, text="Hello world", padding=(200, 200)).pack()
#
# root.mainloop()


# 2. Button
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# greet_button = ttk.Button(root, text="Greet", command=lambda: print("Click button"))
# greet_button.pack(side="left", fill="both", expand=True)
#
# quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# quit_button.pack(side="left")
#
# root.mainloop()


# 3 Greeting app
# import tkinter as tk
# from tkinter import ttk
#
#
# def greet():
#     print(f"Hello, {user_name.get() or 'world'}!")
#
#
# root = tk.Tk()
#
# user_name = tk.StringVar()
#
# name_label = tk.Label(root, text="Name: ")
# name_label.pack(side=tk.LEFT, padx=(50, 50))
# name_entry = tk.Entry(root, textvariable=user_name, width=15)
# name_entry.pack(side=tk.LEFT)
# name_entry.focus()
#
# greet_button = ttk.Button(root, text="Greet", command=greet)
# greet_button.pack(side="left")
#
# quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# quit_button.pack(side="right")
#
# root.mainloop()


# 4. Packing component
# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("1200x700")
# root.title("demo")
# # root.resizable(False, False)
#
# rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
# rectangle_1.pack(side="left",ipadx=10, ipady=10, fill="both", expand=True)
#
# rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
# rectangle_2.pack(ipadx=10, ipady=10, fill="both", side="top", expand=True)
#
# rectangle_3 = tk.Label(root, text="Rectangle 3", bg="black", fg="white")
# rectangle_3.pack(ipadx=10, ipady=10, fill="both", side="left", expand=True)
#
# rectangle_4 = tk.Label(root, text="Rectangle 4", bg="blue", fg="white")
# rectangle_4.pack(ipadx=10, ipady=10, fill="both", side="right", expand=True)
#
# root.mainloop()

# 5. Frame
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.geometry("1200x700")
# root.title("demo")
# # root.resizable(False, False)
#
# main = ttk.Frame(root)
# main.pack(side="left", fill="both", expand=True)
#
# tk.Label(main, text="Label top", bg="red", fg="white").pack(side="top", expand=True, fill="both")
# tk.Label(main, text="Label top", bg="red", fg="white").pack(side="top", expand=True, fill="both")
# tk.Label(root, text="Label left", bg="green", fg="white").pack(
#     side="left", expand=True, fill="both"
# )
#
# root.mainloop()

# 6 Rewrite Greeting app
import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'world'}!")


root = tk.Tk()
root.title("Demo")
root.geometry("1200x800")
root.columnconfigure(0, weight=1)

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky=tk.EW)

name_label = tk.Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = tk.Entry(input_frame, textvariable=user_name, width=15)
name_entry.grid(row=0, column=1)
name_entry.focus()

buttons = ttk.Button(root, padding=(20, 10))
buttons.grid(sticky=tk.EW, row=1, column=0)

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0)
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1)

root.mainloop()
