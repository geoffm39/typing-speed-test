from essential_generators import DocumentGenerator
from wonderwords import RandomWord
from constants import VALID_CHARACTERS, NUMPAD_CHARACTERS

import random


class TestText:
    def __init__(self):
        self.text = ''
        self.word_generator = RandomWord()
        self.paragraph_generator = DocumentGenerator()

    def generate_text(self, test_mode: str):
        if test_mode == 'easy':
            text = self.generate_easy_text()
        elif test_mode == 'hard':
            text = self.generate_hard_text()
        else:
            text = self.generate_numpad_text()
        return text

    def generate_easy_text(self):
        words_list = self.word_generator.random_words(amount=100)
        words = ' '.join(words_list)
        self.text += words
        return words

    def generate_hard_text(self):
        paragraphs = ''
        for _ in range(5):
            paragraph = self.generate_paragraph()
            paragraphs += paragraph
        self.text += paragraphs
        return paragraphs

    def generate_paragraph(self):
        paragraph = self.paragraph_generator.paragraph(min_sentences=10)
        if not self.is_valid_text(paragraph):
            return self.generate_paragraph()
        filtered_paragraph = ''.join(char for char in paragraph if char in VALID_CHARACTERS)
        return filtered_paragraph

    @staticmethod
    def is_valid_text(text):
        return all(char in VALID_CHARACTERS for char in text)

    def generate_numpad_text(self):
        numbers = ''
        for _ in range(500):
            random_digits = [str(random.randint(0, 9)) for _ in range(random.randint(1, 5))]
            random_number = ''.join(random_digits)
            random_character = random.choice(NUMPAD_CHARACTERS)
            numbers += f'{random_number}{random_character}'
        self.text += numbers
        return numbers

    def is_correct_input(self, char, index):
        return char == self.text[index]
