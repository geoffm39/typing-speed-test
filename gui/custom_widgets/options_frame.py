import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from constants import TIMER_OPTIONS


class OptionsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.options = {'time_limit': 1,
                        'mode': 'easy',
                        'backspace': True,
                        }

        time_label = ttk.Label(self, text='Time Limit:')
        self.time_limit = StringVar(value='1 Minute')
        time_combobox = ttk.Combobox(self, textvariable=self.time_limit)
        time_combobox.state(['readonly'])
        time_combobox['values'] = [key for key, value in TIMER_OPTIONS.items()]
        time_combobox.bind('<<ComboboxSelected>>', self.set_time_limit)

        self.backspace_enabled = BooleanVar(value=True)
        backspace_checkbutton = ttk.Checkbutton(self,
                                                text='Backspace',
                                                variable=self.backspace_enabled,
                                                onvalue=True,
                                                offvalue=False)

        mode_label = ttk.Label(self, text='Mode:')
        self.mode = StringVar(value='easy')
        easy = ttk.Radiobutton(self, text='Easy', variable=self.mode, value='easy')
        hard = ttk.Radiobutton(self, text='Hard', variable=self.mode, value='hard')
        numpad = ttk.Radiobutton(self, text='Numpad',
                                 variable=self.mode,
                                 value='numpad',
                                 command=self.show_numlock_warning)

        time_label.grid(column=0, row=0)
        time_combobox.grid(column=1, row=0)
        backspace_checkbutton.grid(column=2, row=0)
        mode_label.grid(column=0, row=1)
        easy.grid(column=1, row=1)
        hard.grid(column=2, row=1)
        numpad.grid(column=3, row=1)

    def set_time_limit(self, event) -> None:
        time_limit_string = self.time_limit.get()
        self.options['time_limit'] = TIMER_OPTIONS[time_limit_string]

    def get_options(self) -> dict:
        self.options['mode'] = self.mode.get()
        self.options['backspace'] = self.backspace_enabled.get()
        return self.options

    @staticmethod
    def show_numlock_warning():
        messagebox.showwarning(title='NumLock', message='Make sure NumLock is on before continuing!')
