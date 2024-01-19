from tkinter import *

from test_text import TestText

class TextFrame(Text):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.configure(font=('Helvetica', 20),
                       spacing2=10,
                       padx=10,
                       pady=10)

        self.test_text = TestText()

        self.cursor_position = 0

    def move_cursor_forwards(self):
        self.cursor_position += 1

    def move_cursor_backwards(self):
        if self.cursor_position < 1:
            return
        self.cursor_position -= 1

    def add_text(self, test_mode):
        text = self.test_text.generate_text(test_mode)
        self.insert('end', text)
