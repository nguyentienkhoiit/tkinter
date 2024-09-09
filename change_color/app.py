from define import *


class App:
    def __init__(self, window):
        window.title("Tinker")
        window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_POSITION_RIGHT}+{WINDOW_POSITION_DOWN}")
        window['background'] = COLOR_BACKGROUND
        # window.resizable(False, False)