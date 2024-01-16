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
        mainframe.grid(column=0, row=0, sticky='nwes')
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(1, weight=1)
        button_frame = ttk.Frame(mainframe)
        button_frame.columnconfigure(0, weight=1)
        button_frame.rowconfigure(0, weight=1)
        button_frame.grid(column=0, row=0, pady=(15, 15), sticky='we')
        test_frame = ttk.Frame(mainframe, borderwidth=5, relief='ridge')
        test_frame.grid(column=0, row=1, padx=50, pady=(0, 50), sticky='nwes')

        self.options_frame = OptionsFrame(test_frame)
        self.text_frame = TextFrame(test_frame)
        self.text_scrollbar = ttk.Scrollbar(test_frame,
                                            orient='vertical',
                                            command=self.text_frame.yview)
        self.text_frame.configure(yscrollcommand=self.text_scrollbar.set)
        self.results_frame = ResultsFrame(test_frame)

        self.start_button = ttk.Button(button_frame, text='Load Text')
        self.restart_test_button = ttk.Button(button_frame)
        self.try_again_button = ttk.Button(button_frame)

        self.start_button.grid(column=0, row=0)
        self.options_frame.grid(column=0, row=1)
