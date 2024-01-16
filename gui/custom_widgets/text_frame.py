from tkinter import *


class TextFrame(Text):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)