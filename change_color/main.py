from tkinter import *
from tkinter import font

from define import *
from app import App

window = Tk()
app = App(window)

fontTitle = font.Font(family='Arial', size=15, weight=font.BOLD)


def change_label_color(name):
    print(f'background is {name}')


def create_button(name, background, column, row=1):
    Button(
        window,
        text=name,
        font=fontTitle,
        padx=20,
        pady=10,
        bg=background,
        fg=COLOR_WHITE,
        command=lambda: change_label_color(background)
    ).grid(row=row, column=column, sticky=EW, padx=30)


Label(
    window,
    text="Hello World!",
    bg=COLOR_PURPLE,
    fg=COLOR_WHITE,
    padx=30,
    pady=20,
    font=fontTitle
).grid(row=0, column=0, columnspan=4, sticky='wse', padx=30)

create_button("Green", COLOR_GREEN, 0, 1)
create_button("Blue", COLOR_BLUE, 1, 1)
create_button("Red", COLOR_RED, 2, 1)
create_button("Yellow", COLOR_YELLOW, 3, 1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.mainloop()
