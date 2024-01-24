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
        self.backspace_count = 0
        self.keypress_count = 0

        self.tag_configure('correct', foreground='green')
        self.tag_configure('incorrect', foreground='red')

    def move_cursor_forwards(self):
        self.cursor_position += 1

    def move_cursor_backwards(self):
        if self.cursor_position < 1:
            return
        self.cursor_position -= 1

    def reset_cursor(self):
        self.cursor_position = 0

    def set_options(self, test_mode, backspace_allowed):
        self.test_mode = test_mode
        self.backspace_allowed = backspace_allowed

    def add_text(self):
        text = self.test_text.generate_text(self.test_mode)
        self.configure(state='normal')
        self.insert('end', text)
        self.configure(state='disabled')
        self.update_idletasks()

    def clear_text(self):
        self.test_text.reset_text()
        self.configure(state='normal')
        self.delete('1.0', 'end')
        self.configure(state='disabled')
        self.reset_cursor()

    def process_keyboard_input(self, event):
        self.keypress_count += 1
        if self.is_nearing_end_of_text():
            self.add_text()
        self.move_cursor_into_view()
        if self.is_modifier_key(event):
            return
        if self.is_backspace_keypress(event):
            self.process_backspace_keypress()
            return
        if self.is_numpad_mode():
            self.process_numpad_input(event)
            return
        if self.is_space_keypress(event):
            self.process_space_keypress()
            return
        self.apply_relevant_tag(event)
        self.move_cursor_forwards()

    @staticmethod
    def is_modifier_key(event):
        return event.keysym in MODIFIER_KEYS

    @staticmethod
    def is_backspace_keypress(event):
        return event.keysym == 'BackSpace'

    @staticmethod
    def is_enter_keypress(event):
        return event.keysym == 'Return'

    @staticmethod
    def is_space_keypress(event):
        return event.char == ' '

    def is_numpad_mode(self):
        return self.test_mode == 'numpad'

    def is_nearing_end_of_text(self):
        return self.compare(f'1.{self.cursor_position + 50}', '>=', '1.end')

    def move_cursor_into_view(self):
        self.see(f'1.{self.cursor_position} + 2c')

    def apply_relevant_tag(self, event):
        if self.test_text.is_correct_input(event.char, self.cursor_position):
            self.set_char_tag('correct')
        else:
            self.set_char_tag('incorrect')

    def set_char_tag(self, tag):
        self.tag_add(tag, f'1.{self.cursor_position}')

    def process_numpad_input(self, event):
        if self.is_enter_keypress(event):
            self.process_space_keypress()
            return
        self.apply_relevant_tag(event)
        self.move_cursor_forwards()

    def process_backspace_keypress(self):
        if self.backspace_allowed:
            self.backspace_count += 1
            self.move_cursor_backwards()
            self.remove_tags_at_index(self.cursor_position)
        else:
            self.remove_tags_at_index(self.cursor_position)
            self.set_char_tag('incorrect')
            self.move_cursor_forwards()

    def process_space_keypress(self):
        if self.test_text.is_correct_input(' ', self.cursor_position):
            self.set_char_tag('correct')
            self.move_cursor_forwards()
        else:
            self.jump_to_next_word()

    def jump_to_next_word(self):
        self.set_char_tag('incorrect')
        self.move_cursor_forwards()
        if not self.is_space(self.cursor_position):
            return self.jump_to_next_word()
        self.set_char_tag('correct')
        self.move_cursor_forwards()

    def is_space(self, index):
        return self.get(f'1.{index}') == ' '

    def remove_tags_at_index(self, index):
        for tag in self.tag_names(f'1.{index}'):
            self.tag_remove(tag, f'1.{index}')

    def get_test_data(self):
        results = {'correct_words': 0,
                   'incorrect_words': 0,
                   'correct_chars': 0,
                   'incorrect_chars': 0,
                   'backspace_count': self.backspace_count,
                   'keys_pressed': self.keypress_count}
        wrong_word_flag = False
        for index in range(self.test_text.get_text_char_count()):
            if not self.char_has_tag(index):
                return results
            if self.is_space(index):
                if self.char_has_incorrect_tag(index):
                    results['incorrect_chars'] += 1
                else:
                    results['correct_chars'] += 1
                if wrong_word_flag:
                    results['incorrect_words'] += 1
                else:
                    results['correct_words'] += 1
                wrong_word_flag = False
                continue
            if self.char_has_incorrect_tag(index):
                results['incorrect_chars'] += 1
                wrong_word_flag = True
            else:
                results['correct_chars'] += 1
        return results

    def char_has_tag(self, index):
        return bool(self.tag_names(f'1.{index}'))

    def char_has_incorrect_tag(self, index):
        return self.tag_names(f'1.{index}')[0] == 'incorrect'
