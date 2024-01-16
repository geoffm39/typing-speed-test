from tkinter import *
from tkinter import ttk

from gui.custom_widgets.text_frame import TextFrame
from gui.custom_widgets.results_frame import ResultsFrame
from gui.custom_widgets.options_frame import OptionsFrame


class MainWindow:
    def __init__(self, root: Tk):
        root.title('Typing Speed Test')
        root.iconbitmap('gui/keyboard_icon.ico')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(1, weight=1)

        self.button_frame = ttk.Frame(mainframe)
        self.button_frame.grid(column=0, row=0, sticky=(W, E))

        self.test_frame = ttk.Frame(mainframe, borderwidth=5, relief='ridge')
        self.test_frame.grid(column=0, row=1, sticky=(N, W, E, S))
