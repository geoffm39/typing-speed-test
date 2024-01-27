from tkinter import *
from tkinter import ttk

from test_result import TestResult


class ResultsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.mode_string = StringVar()
        self.mode_label = ttk.Label(self, textvariable=self.mode_string)
        self.mode_label.grid(column=0, row=0, columnspan=2, sticky='we', pady=5)

        self.result_labelframe = ttk.Labelframe(self, text='Test Results: ', padding=10)
        self.result_labelframe.grid(column=0, row=1, padx=10)
        self.highscore_labelframe = ttk.Labelframe(self, text='Highscore: ', padding=10)
        self.highscore_labelframe.grid(column=1, row=1, padx=10)

        self.wpm = StringVar()
        self.wpm_label = ttk.Label(self.result_labelframe, textvariable=self.wpm)
        self.cpm = StringVar()
        self.cpm_label = ttk.Label(self.result_labelframe, textvariable=self.cpm)
        self.kpm = StringVar()
        self.kpm_label = ttk.Label(self.result_labelframe, textvariable=self.kpm)
        self.accuracy = StringVar()
        self.accuracy_label = ttk.Label(self.result_labelframe, textvariable=self.accuracy)
        self.backspaces = StringVar()
        self.backspaces_label = ttk.Label(self.result_labelframe, textvariable=self.backspaces)

        self.wpm_label.grid(column=0, row=0)
        self.cpm_label.grid(column=0, row=1)
        self.kpm_label.grid(column=0, row=2)
        self.accuracy_label.grid(column=0, row=3)
        self.backspaces_label.grid(column=0, row=4)

        self.wpm_highscore = StringVar()
        self.wpm_highscore_label = ttk.Label(self.highscore_labelframe, textvariable=self.wpm_highscore)
        self.cpm_highscore = StringVar()
        self.cpm_highscore_label = ttk.Label(self.highscore_labelframe, textvariable=self.cpm_highscore)
        self.kpm_highscore = StringVar()
        self.kpm_highscore_label = ttk.Label(self.highscore_labelframe, textvariable=self.kpm_highscore)
        self.accuracy_highscore = StringVar()
        self.accuracy_highscore_label = ttk.Label(self.highscore_labelframe, textvariable=self.accuracy_highscore)
        self.backspaces_highscore = StringVar()
        self.backspaces_highscore_label = ttk.Label(self.highscore_labelframe, textvariable=self.backspaces_highscore)

        self.wpm_highscore_label.grid(column=0, row=0)
        self.cpm_highscore_label.grid(column=0, row=1)
        self.kpm_highscore_label.grid(column=0, row=2)
        self.accuracy_highscore_label.grid(column=0, row=3)
        self.backspaces_highscore_label.grid(column=0, row=4)

        self.test_result = TestResult()

    def show_results(self, test_data):
        self.test_result.calculate_test_results(test_data)
        self.mode_string.set(value=f"{test_data['mode'].title()} Mode")
        self.set_results()
        self.set_highscore(test_data)

    def set_results(self):
        results = self.test_result.get_test_results()
        self.wpm.set(value=f'WPM: {results["wpm"]}')
        self.cpm.set(value=f'CPM: {results["cpm"]}')
        self.kpm.set(value=f'KPM: {results["kpm"]}')
        self.accuracy.set(value=f'Accuracy: {results["accuracy"]}')
        self.backspaces.set(value=f'Backspaces: {results["backspaces"]}')

    def set_highscore(self, test_data):
        high_score = self.test_result.get_highscores()[test_data['mode']]
        self.wpm_highscore.set(value=f'WPM: {high_score["wpm"]}')
        self.cpm_highscore.set(value=f'CPM: {high_score["cpm"]}')
        self.kpm_highscore.set(value=f'KPM: {high_score["kpm"]}')
        self.accuracy_highscore.set(value=f'Accuracy: {high_score["accuracy"]}')
        self.backspaces_highscore.set(value=f'Backspaces: {high_score["backspaces"]}')
