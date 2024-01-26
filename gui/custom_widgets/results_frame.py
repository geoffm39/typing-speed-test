from tkinter import *
from tkinter import ttk

from test_result import TestResult


class ResultsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.test_result = TestResult()

    def show_results(self, test_data):
        self.test_result.calculate_test_results(test_data)
        results = self.test_result.get_test_results()
        print(results)