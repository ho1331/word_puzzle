# My solution

So let's get started.
* First of all, we should define a function. I have called it 'puzzle_length'

```
def puzzle_length(start_word: str, end_word: str, dict_file) -> list:
```

it takes three positional arguments: start word, end word and dict_file (now a word list). The fourth argument should be
the path to the result, but I will implement this later.

* Secondly, I should check that the `end word` is not equal to `start word` and `end word` is in our `dict_file`. If these are true - we return '0'

```
    if end_word not in dict_file or start_word == end_word:
        return 0
```

* In the next step we should define a queue for checking our pattern and sequence of visited words

```
from collections import deque
...

    queue = deque()
    visited = []
    queue.append((start_word, []))    # add start_word to queue and list of steps to the end_word

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
        for char in range(len(word)):
            for new_char in range(ord('a'), ord('z')+1):
                next_word = f'{word[:char]}{chr(new_char)}{word[char+1:]}'   # replace char for each of alphabet symbol
```

* Finally, check if the next_word is equal to the end_word. If not - add this word into our queue and continue processing

```
            if next_word == end_word:
                steps.append(end_word)
                return steps

            elif next_word not in visited and next_word in words:
                visited.append(next_word)
                queue.append((next_word, steps[:]))
```

* Also, we forgot about our dictfile and result file. I'm going to do it like this:

```
    import os
    import json
    ...


    def words_reader(filename):
        file = os.path.abspath(filename)
        with open(file, 'r') as f:
            data = json.loads(f.read())

        return data


    def steps_writter(words, path):
        with open(f'{path}/result.txt', 'w+') as f:
            f.write(','.join(words))
    
    ...
    ...
```

> Finally, correct our function with the previous changes:

```
import os
import json
from collections import deque


def words_reader(filename):
    ...

def steps_writter(words, path):
    ...


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
```

## References
1. https://towardsdatascience.com/search-algorithm-breadth-first-search-with-python-50571a9bb85e