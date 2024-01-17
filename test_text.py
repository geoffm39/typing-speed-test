from essential_generators import DocumentGenerator
from wonderwords import RandomWord

# Standard characters and symbols on an American keyboard
VALID_CHARACTERS = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
]


class TestText:
    def __init__(self):
        self.text = ''
        self.word_generator = RandomWord()
        self.paragraph_generator = DocumentGenerator()

    def generate_text(self, mode: str):
        if mode == 'easy':
            self.generate_easy_text()
        elif mode == 'hard':
            self.generate_hard_text()
        else:
            self.generate_numbers()

    def generate_easy_text(self):
        words_list = self.word_generator.random_words(amount=500)
        words = ' '.join(words_list)
        self.text += words
        print(self.text)

    def generate_hard_text(self):
        for _ in range(5):
            paragraph = self.generate_paragraph()
            self.text += paragraph
        print(self.text)

    def generate_paragraph(self):
        paragraph = self.paragraph_generator.paragraph(min_sentences=10)
        if not self.is_valid_text(paragraph):
            self.generate_paragraph()
        filtered_paragraph = ''.join(char for char in paragraph if char in VALID_CHARACTERS)
        return filtered_paragraph

    @staticmethod
    def is_valid_text(text):
        return all(char in VALID_CHARACTERS for char in text)

    def generate_numbers(self):
        pass
