import json

from constants import DEFAULT_HIGHSCORE_JSON


class TestResult:
    def __init__(self):
        self.test_results = {'wpm': 0,
                             'cpm': 0,
                             'kpm': 0,
                             'accuracy': '',
                             'backspaces': 0}

        self.high_scores = self.load_highscore_json()

    def calculate_test_results(self, test_data):
        minutes = test_data['minutes']
        self.calculate_wpm(test_data['correct_words'], minutes)
        self.calculate_cpm(test_data['correct_chars'], minutes)
        self.calculate_kpm(test_data['keys_pressed'], minutes)
        self.calculate_accuracy(test_data['correct_chars'], test_data['incorrect_chars'])
        self.test_results['backspaces'] = test_data['backspace_count']
        if self.is_highscore(test_data):
            self.set_highscore(test_data)

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

    def is_highscore(self, test_data):
        return self.test_results['wpm'] > self.high_scores[test_data['mode']]['wpm']

    def load_highscore_json(self):
        try:
            high_scores = self.read_json_file()
        except FileNotFoundError:
            high_scores = self.create_json_file()
        return high_scores

    @staticmethod
    def read_json_file():
        with open('high_scores.json', 'r') as file:
            high_scores = json.load(file)
        return high_scores

    @staticmethod
    def create_json_file():
        high_scores = DEFAULT_HIGHSCORE_JSON
        with open('high_scores.json', 'w') as file:
            json.dump(high_scores, file, indent=4)
        return high_scores

    def get_highscores(self):
        return self.high_scores

    def set_highscore(self, test_data):
        self.high_scores[test_data['mode']] = dict(self.test_results)
        self.save_highscores_to_json()

    def save_highscores_to_json(self):
        with open('high_scores.json', 'w') as file:
            json.dump(self.get_highscores(), file, indent=4)
