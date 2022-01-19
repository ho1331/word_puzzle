import logging
import logging.config
import sys

from collections import deque
from string import ascii_lowercase
from typing import Union

from src.utils import (
    steps_writter,
    words_reader,
)
from src.utils import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def puzzle_length(start_word: str, end_word: str, dict_file: str, result_path: str) -> Union[list, None]:
    """
    This function calculates the shortest path of four-letter words
    beginning with start_word and ending with end_word

    Args:
        start_word (str): a four letter word
        end_word (str): a four letter word
        dict_file (str): the file name of a text file containing four letter words
        result_path (str): the path to some directory

    Returns:
        list: the shortest list of four letter words,
              starting with start_word, and ending with end_word
    """
    words = set(words_reader(dict_file))

    if start_word == end_word:
        msg = f'Equal words: "start_word"={start_word}, "end_word"={end_word}'
        logger.info(msg)
        sys.exit(msg)

    if end_word not in words:
        msg = f'The word "{end_word}" is not in "{dict_file}"'
        logger.info(msg)
        sys.exit(msg)

    queue = deque()
    queue.append((start_word, []))

    while len(queue) > 0:
        word, steps = queue.popleft()
        steps.append(word)

        for char in range(len(word)):
            for new_char in ascii_lowercase:
                next_word = f'{word[:char]}{new_char}{word[char+1:]}'

                if next_word == end_word:
                    steps.append(end_word)
                    steps_writter(steps, result_path)
                    return steps

                elif next_word in words:
                    words.remove(next_word)
                    queue.append((next_word, steps[:]))

    msg = f'The path from "{start_word}" to "{end_word}" does not not exist'
    logger.info(msg)
    sys.exit(msg)
