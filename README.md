# My solution
### Runtime
* The application is written in python 3.8
### Running a script
```
$ python main.py wows rays tests/test_data.txt .
```
## So let's get started.
* First of all, we should define a function. I have called it `puzzle_length`

```
def puzzle_length(start_word: str, end_word: str, dict_file: list) -> Union[list, None]:
```

it takes three positional arguments: start word, end word and dict_file (now a word list). The fourth argument should be
the path to the result, but I will implement this later.

* Secondly, I should check that the `end word` is not equal to `start word` and `end word` is in our `dict_file`. If these are true - we interrupt program execution.

```
    import sys
    ...
    words = set(dict_file) # set our dict_file to remove duplicates

    if start_word == end_word:
        msg = f'Equal words: "start_word"={start_word}, "end_word"={end_word}'
        sys.exit(msg)

    if end_word not in words:
        msg = f'The word "{end_word}" is not in "{dict_file}"'
        sys.exit(msg)

```

* In the next step we should define a queue for checking our pattern

```
from collections import deque
...

    queue = deque()
    queue.append((start_word, []))    # add start_word to queue and empty list for our steps

```

* So, we are going to go through the loops: while loop and nested for loops (for each char):

```
    while len(queue) > 0:
        word, steps = queue.popleft()
        steps.append(word)
```
here we take the last word of the queue and put this word into our path of words (mean 'steps')

and going through the loops for each char for each word

```
    from string import ascii_lowercase
    ...

        for char in range(len(word)):
            for new_char in ascii_lowercase:
                next_word = f'{word[:char]}{new_char}{word[char+1:]}'   # replace char for each of alphabet symbol
```

* Finally, check if the next_word is equal to the end_word. If not - add this word into our queue and continue processing

```
            if next_word == end_word:
                steps.append(end_word)
                return steps

            elif next_word in words:
                words.remove(next_word) # remove checked word
                queue.append((next_word, steps[:]))
```

* Also, we forgot about our dictfile and result file. I'm going to do it like this:

```
    # utils.py
    import json
    import os
    ...


    def words_reader(filename):
        file = os.path.abspath(filename)
        try:
            with open(path, 'r') as file:
                data = json.loads(file.read())
        except FileNotFoundError as exp:
            ...
            raise

        return data


    def steps_writter(words, path):
        try:
            with open(f'{path}/result.txt', 'w+') as file:
                file.write(','.join(words))
        except FileNotFoundError as exp:
            ...
            raise
    
        ...
        ...
```
#### Note: we are using get_parse_args() to incorporate the parsing of command line arguments and logging module from standart python library to implement a flexible event logging system for our application
_
_
_
> Finally, correct our function with the previous changes:

```
# word_puzzle.py

import logging
import logging.config
import sys

from collections import deque
from string import ascii_lowercase
from typing import Union

from utils import (
    steps_writter,
    words_reader,
)
from utils import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def puzzle_length(start_word: str, end_word: str, dict_file: str, result_path: str) -> Union[list, None]:
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
```
#### I followed YAGNI and KISS principles in solving the problem.
## References
1. https://towardsdatascience.com/search-algorithm-breadth-first-search-with-python-50571a9bb85e
2. https://docs.python.org/3/library/logging.html
3. https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
