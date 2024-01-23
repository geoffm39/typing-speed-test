class TestResult:
    def __init__(self):
        self.text_results = {'wpm': None,
                             'cpm': None,
                             'kpm': None,
                             'accuracy': None,
                             'backspaces': None}

        self.numpad_results = {'npm': None,
                               'cpm': None,
                               'kpm': None,
                               'accuracy': None,
                               'backspaces': None}

    def calculate_text_results(self, test_data):
        pass

    def calculate_numpad_results(self, test_data):
        pass

    def get_test_results(self):
        pass

    def is_highscore(self):
        pass

    def get_highscore(self):
        pass

    def set_highscore(self):
        pass
