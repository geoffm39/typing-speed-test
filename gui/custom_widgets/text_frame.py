from tkinter import *

from test_text import TestText
from constants import MODIFIER_KEYS


class TextFrame(Text):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.configure(font=('Helvetica', 20),
                       spacing2=10,
                       padx=10,
                       pady=10)

        self.test_text = TestText()

        self.cursor_position = 0
        self.test_mode = None
        self.backspace_allowed = True

        self.tag_configure('correct', foreground='green')
        self.tag_configure('incorrect', foreground='red')

    def move_cursor_forwards(self):
        self.cursor_position += 1

    def move_cursor_backwards(self):
        if self.cursor_position < 1:
            return
        self.cursor_position -= 1

    def set_options(self, test_mode, backspace_allowed):
        self.test_mode = test_mode
        self.backspace_allowed = backspace_allowed

    def add_text(self):
        text = self.test_text.generate_text(self.test_mode)
        self.insert('end', text)

    def process_keyboard_input(self, event):
        self.see(f'1.{self.cursor_position} + 2c')
        if self.is_modifier_key(event):
            return
        if self.is_backspace(event):
            self.process_backspace_keypress()
            return
        if self.is_numpad_mode():
            self.process_numpad_input(event)
            return
        if self.is_space(event):
            self.process_space_keypress()
            return
        self.apply_relevant_tag(event)
        self.move_cursor_forwards()

    @staticmethod
    def is_modifier_key(event):
        return event.keysym in MODIFIER_KEYS

    @staticmethod
    def is_backspace(event):
        return event.keysym == 'BackSpace'

    @staticmethod
    def is_enter(event):
        return event.keysym == 'Return'

    @staticmethod
    def is_space(event):
        return event.char == ' '

    def is_numpad_mode(self):
        return self.test_mode == 'numpad'

    def apply_relevant_tag(self, event):
        if self.test_text.is_correct_input(event.char, self.cursor_position):
            self.set_char_tag('correct')
        else:
            self.set_char_tag('incorrect')

    def set_char_tag(self, tag):
        self.tag_add(tag, f'1.{self.cursor_position}')

    def process_numpad_input(self, event):
        if self.is_enter(event):
            self.process_space_keypress()
            return
        self.apply_relevant_tag(event)
        self.move_cursor_forwards()

    def process_backspace_keypress(self):
        if self.backspace_allowed:
            self.move_cursor_backwards()
            self.remove_tags_at_index(self.cursor_position)
        else:
            self.remove_tags_at_index(self.cursor_position)
            self.set_char_tag('incorrect')
            self.move_cursor_forwards()

    def process_space_keypress(self):
        if self.test_text.is_correct_input(' ', self.cursor_position):
            self.move_cursor_forwards()
        else:
            self.jump_to_next_word()

    def jump_to_next_word(self):
        self.set_char_tag('incorrect')
        self.move_cursor_forwards()
        if not self.test_text.is_correct_input(' ', self.cursor_position):
            return self.jump_to_next_word()
        self.move_cursor_forwards()

    def remove_tags_at_index(self, index):
        for tag in self.tag_names(f'1.{index}'):
            self.tag_remove(tag, f'1.{index}')
