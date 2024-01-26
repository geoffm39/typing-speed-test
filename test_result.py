class TestResult:
    def __init__(self):
        self.test_results = {'wpm': 0,
                             'cpm': 0,
                             'kpm': 0,
                             'accuracy': '',
                             'backspaces': 0}

    def calculate_test_results(self, test_data):
        minutes = test_data['minutes']
        self.calculate_wpm(test_data['correct_words'], minutes)
        self.calculate_cpm(test_data['correct_chars'], minutes)
        self.calculate_kpm(test_data['keys_pressed'], minutes)
        self.calculate_accuracy(test_data['correct_chars'], test_data['incorrect_chars'])
        self.test_results['backspaces'] = test_data['backspace_count']

    def calculate_wpm(self, correct_words, minutes):
        wpm = correct_words // minutes
        self.test_results['wpm'] = int(wpm)

    def calculate_cpm(self, correct_chars, minutes):
        cpm = correct_chars // minutes
        self.test_results['cpm'] = int(cpm)

    def calculate_kpm(self, keys_pressed, minutes):
        kpm = keys_pressed // minutes
        self.test_results['kpm'] = int(kpm)

    def calculate_accuracy(self, correct_chars, incorrect_chars):
        total_chars = correct_chars + incorrect_chars
        accuracy_percentage = correct_chars / total_chars * 100
        percentage_string = f'{round(accuracy_percentage)}%'
        self.test_results['accuracy'] = percentage_string

    def get_test_results(self):
        return self.test_results

    def is_highscore(self):
        pass

    def get_highscore(self):
        pass

    def set_highscore(self):
        pass
