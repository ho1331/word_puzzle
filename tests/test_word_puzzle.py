import os
from puzzle.word_puzzle import puzzle_length


DATA = 'test_data.txt'
RES_PATH = os.path.curdir
START_WORD = "wows"
STOP_WORD = "rays"


def test_pazzle_length():
    words = puzzle_length(START_WORD, STOP_WORD, DATA, RES_PATH)

    assert words == ['wows', 'bows', 'bobs', 'gobs', 'gabs', 'gays', 'rays']


def test_pazzle_length_write_data():
    puzzle_length(START_WORD, STOP_WORD, DATA, RES_PATH)
    file = os.path.abspath('result.txt')

    with open(file, 'r') as f:
        result = f.read().split(',')

    assert result == ['wows', 'bows', 'bobs', 'gobs', 'gabs', 'gays', 'rays']
