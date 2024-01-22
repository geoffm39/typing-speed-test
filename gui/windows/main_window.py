from tkinter import *
from tkinter import ttk

from gui.custom_widgets.text_frame import TextFrame
from gui.custom_widgets.results_frame import ResultsFrame
from gui.custom_widgets.options_frame import OptionsFrame
from test_result import TestResult


class MainWindow:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title('Typing Speed Test')
        self.root.iconbitmap('gui/keyboard_icon.ico')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(self.root)
        mainframe.grid(column=0, row=0, sticky='nwes')
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(1, weight=1)
        button_frame = ttk.Frame(mainframe)
        button_frame.columnconfigure(0, weight=1)
        button_frame.rowconfigure(0, weight=1)
        button_frame.grid(column=0, row=0, pady=(15, 15), sticky='we')
        test_frame = ttk.Frame(mainframe, borderwidth=5, relief='ridge')
        test_frame.grid(column=0, row=1, padx=50, pady=(0, 50), sticky='nwes')
        test_frame.columnconfigure(0, weight=1)

        self.options_frame = OptionsFrame(test_frame)
        self.text_frame = TextFrame(test_frame, width=80, height=10, wrap='word', takefocus=0)
        self.text_scrollbar = ttk.Scrollbar(test_frame,
                                            orient='vertical',
                                            command=self.text_frame.yview)
        self.text_frame.configure(yscrollcommand=self.text_scrollbar.set)
        self.results_frame = ResultsFrame(test_frame)

        self.start_button = ttk.Button(button_frame, text='Generate Text', command=self.apply_options)
        self.restart_test_button = ttk.Button(button_frame)
        self.try_again_button = ttk.Button(button_frame)

        self.start_button.grid(column=0, row=0)
        self.options_frame.grid(column=0, row=0)

    def on_key_press(self, event):
        self.text_frame.process_keyboard_input(event)

    def apply_options(self):
        options = self.options_frame.get_options()
        self.text_frame.set_options(options['mode'], options['backspace'])
        self.text_frame.add_text()
        self.text_frame.configure(state='disabled')

        self.root.bind('<Key>', self.on_key_press)

        self.start_button.configure(state='disabled')
        self.start_button.grid_forget()
        self.text_frame.grid(column=0, row=0)
        self.text_scrollbar.grid(column=1, row=0, sticky='ns')
