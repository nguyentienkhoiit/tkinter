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
import tkinter as tk

root = tk.Tk()
root.geometry("400x600")
root.title("demo")
root.resizable(False, False)

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(ipadx=10, ipady=10, fill="x")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(ipadx=10, ipady=10)

root.mainloop()
