import logging

import pytest

from puzzle.word_puzzle import puzzle_length
from tests.conftest import (
    CLEAR_WORDS,
    DATA_PATH,
    RES_PATH,
)


logging.disable(logging.CRITICAL)


@pytest.mark.parametrize('start_word, end_word', CLEAR_WORDS)
def test_puzzle_length(start_word, end_word, tmpdir):
    words = puzzle_length(start_word, end_word, DATA_PATH, tmpdir)
    assert len(words) > 0


def test_puzzle_length_write_data(tmpdir):
    puzzle_length('wows', 'rays', DATA_PATH, tmpdir)
    path = tmpdir.join('result.txt')
    with open(path, 'r') as file:
        result = file.read().split(',')

    assert result == ['wows', 'bows', 'bobs', 'gobs', 'gabs', 'gays', 'rays']


@pytest.mark.parametrize('start_word, end_word', CLEAR_WORDS)
def test_wrong_data_path(start_word, end_word):
    with pytest.raises(FileNotFoundError):
        puzzle_length(start_word, end_word, 'test_path/test_data.txt', RES_PATH)


@pytest.mark.parametrize('start_word, end_word', CLEAR_WORDS)
def test_wrong_result_path(start_word, end_word):
    with pytest.raises(FileNotFoundError):
        puzzle_length(start_word, end_word, DATA_PATH, 'test_path/result.txt')


@pytest.mark.parametrize('start_word, end_word', [('wows', 'wows'), ("rays", 'rays')])
def test_equal_words(start_word, end_word):
    with pytest.raises(SystemExit) as exc_info:
        puzzle_length(start_word, end_word, DATA_PATH, RES_PATH)
    assert str(exc_info.value) == f'Equal words: "start_word"={start_word}, "end_word"={end_word}'


@pytest.mark.parametrize('start_word, end_word', [('wows', 'rfff'), ("rays", 'ssss')])
def test_presence_in_dict(start_word, end_word):
    with pytest.raises(SystemExit) as exc_info:
        puzzle_length(start_word, end_word, DATA_PATH, RES_PATH)
    assert str(exc_info.value) == f'The word "{end_word}" is not in "{DATA_PATH}"'


@pytest.mark.parametrize('start_word, end_word', [('wows', 'viva'), ('dopy', 'egos')])
def test_empty_result(start_word, end_word):
    with pytest.raises(SystemExit) as exc_info:
        puzzle_length(start_word, end_word, DATA_PATH, RES_PATH)
    assert str(exc_info.value) == f'The path from "{start_word}" to "{end_word}" does not not exist'
