import os
import json
from collections import deque


def words_reader(filename):
    file = os.path.abspath(filename)
    with open(file, 'r') as f:
        data = json.loads(f.read())

    return data


def steps_writter(words, path):
    with open(f'{path}/result.txt', 'w+') as f:
        f.write(','.join(words))


def puzzle_length(start_word: str, end_word: str, dict_file, result_path) -> list:
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
