from tkinter import *
from tkinter import ttk

from test_result import TestResult


class ResultsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.test_result = TestResult()

