from tkinter import *
from tkinter import font

from define import *
from app import App

window = Tk()
app = App(window)


def show_hello():
    print("Hello World!")


def show_course(name):
    print(f'show course {name}')


fontTitle = font.Font(family='Arial', size=30, weight=font.BOLD)
fontText = font.Font(family='Arial', size=20)

btnHello = Button(
    window,
    text='Hello',
    font=fontTitle,
    padx=30,
    pady=20,
    activebackground=COLOR_PURPLE,
    bg=COLOR_YELLOW,
    fg=COLOR_RED,
    command=lambda : show_course('')
)
btnHello.grid(row=0, column=0)

btnPython = Button(
    window,
    text='Python',
    font=fontTitle,
    padx=30,
    pady=20,
    activebackground=COLOR_PURPLE,
    bg=COLOR_YELLOW,
    fg=COLOR_RED,
    command=lambda: show_course('Python')
)
btnPython.grid(row=0, column=1)

btnTkinter = Button(
    window,
    text='Tkinter',
    font=fontTitle,
    padx=30,
    pady=20,
    activebackground=COLOR_PURPLE,
    bg=COLOR_YELLOW,
    fg=COLOR_RED,
    command=lambda: show_course('Tkinter')
)
btnTkinter.grid(row=0, column=2)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
