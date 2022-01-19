import logging
from unittest.mock import patch

import pytest

from src.utils import (
    get_parse_args,
    steps_writter,
    words_reader,
)
from tests.conftest import (
    DATA_PATH,
    RES_PATH,
)


logging.disable(logging.CRITICAL)


def test_get_parse_args():
    with patch('argparse._sys.argv', ['word_puzzle.py', 'wows', 'rays', DATA_PATH, RES_PATH]):
        args = get_parse_args()
    assert vars(args) == {
            'start': 'wows',
            'end': 'rays',
            'words': 'tests/test_data.txt',
            'result_path': '.'
        }


@pytest.mark.parametrize(
    'start_word, end_word, data, res_path',
    [
        ('wowss', 'rays', DATA_PATH, RES_PATH),
        ('wows', 'rayds', DATA_PATH, RES_PATH),
        ('wows', 'rays', './data.txt', RES_PATH),
        ('wowss', 'rays', DATA_PATH, './result.txt'),
    ]
)
def test_get_parse_args_fail(start_word, end_word, data, res_path):
    with patch('argparse._sys.argv', ['word_puzzle.py', start_word, end_word, data, res_path]):
        with pytest.raises(SystemExit):
            get_parse_args()


def test_steps_writer(tmpdir):
    test_words = ['test1', 'test2', 'test3']
    steps_writter(test_words, tmpdir)

    path = tmpdir.join('result.txt')
    with open(path, 'r') as file:
        words = file.readlines()

    assert words == ['test1,test2,test3']


def test_steps_writter_fail():
    with pytest.raises(FileNotFoundError):
        steps_writter(['word1', 'word2'], './result')


def test_words_reader():
    data = words_reader(DATA_PATH)
    assert isinstance(data, list)


def test_words_reader_fail():
    with pytest.raises(FileNotFoundError):
        words_reader("test_data.txt")
