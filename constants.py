VALID_CHARACTERS = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
]

NUMPAD_CHARACTERS = ['+', '-', '*', '/', '.', '.', ' ', ' ', ' ', ' ', ' ', ' ']

MODIFIER_KEYS = ['Tab', 'Shift_L', 'Shift_R', 'Num_Lock']

TIMER_OPTIONS = {'1 Minute': 1,
                 '3 Minutes': 3,
                 '5 Minutes': 5,
                 '10 Minutes': 10,
                 'Marathon!': None}

DEFAULT_HIGHSCORE_JSON = {'easy': {'wpm': 0,
                                   'cpm': 0,
                                   'kpm': 0,
                                   'accuracy': '',
                                   'backspaces': 0},
                          'hard': {'wpm': 0,
                                   'cpm': 0,
                                   'kpm': 0,
                                   'accuracy': '',
                                   'backspaces': 0},
                          'numpad': {'wpm': 0,
                                     'cpm': 0,
                                     'kpm': 0,
                                     'accuracy': '',
                                     'backspaces': 0}}
