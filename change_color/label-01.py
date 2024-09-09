from tkinter import *
from tkinter import font

from define import *
from app import App

window = Tk()
app = App(window)

print(font.families())

font_tite = font.Font(family='Arial', size=30, weight=font.BOLD)
font_text = font.Font(family='Arial', size=20)

# label
label_python = Label(
    window,
    text="Python",
    bg=COLOR_RED,
    fg=COLOR_WHITE,
    width=5,
    padx=20,
    pady=10,
    font=font_tite
)
label_python.pack(anchor=NW)

label_tkinter = Label(
    window,
    text="Tkinter",
    bg=COLOR_RED,
    fg=COLOR_WHITE,
    width=5,
    padx=20,
    pady=10,
    font=font_tite
)
label_tkinter.pack(side=BOTTOM, anchor=SE)


window.mainloop()
