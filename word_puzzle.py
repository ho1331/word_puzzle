from collections import deque

from utils import (
    get_parse_args,
    steps_writter,
    words_reader,
)


def puzzle_length(start_word: str, end_word: str, dict_file: str, result_path: str) -> list:
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
    words = words_reader(dict_file)

    if end_word not in words or start_word == end_word:
        return 0

    queue = deque()
    visited = [start_word]

    queue.append((start_word, []))

    while len(queue) > 0:
        word, steps = queue.popleft()
        steps.append(word)

        for char in range(len(word)):
            for new_char in range(ord('a'), ord('z')+1):
                next_word = f'{word[:char]}{chr(new_char)}{word[char+1:]}'

                if next_word == end_word:
                    steps.append(end_word)
                    steps_writter(steps, result_path)
                    return steps

                elif next_word not in visited and next_word in words:
                    visited.append(next_word)
                    queue.append((next_word, steps[:]))

    return 0

if __name__ == '__main__':
    args = get_parse_args()

    start_word = args.start
    end_word = args.end
    dict_file = args.words
    res_path = args.result_path

    puzzle_length(start_word, end_word, dict_file, res_path)
