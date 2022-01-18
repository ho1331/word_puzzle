import os


DATA_PATH = 'tests/test_data.txt'
RES_PATH = os.path.curdir

START_WORDS = ["wows", "yank", "thar", "curl", "venn"]
STOP_WORDS = ["rays", "ross", "tour", "ants", "lean"]

CLEAR_WORDS = [(start_word, end_word) for start_word, end_word in zip(START_WORDS, STOP_WORDS)]
