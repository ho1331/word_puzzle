import argparse
import os
import json


def words_reader(filename):
    file = os.path.abspath(filename)
    with open(file, 'r') as file:
        data = json.loads(file.read())

    return data


def steps_writter(words, path):
    with open(f'{path}/result.txt', 'w+') as file:
        file.write(','.join(words))


def get_parse_args():
    """
    Parses command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'start',
        type=str,
        help='The start word.'
    )
    parser.add_argument(
        'end',
        type=str,
        help='The end word.'
    )
    parser.add_argument(
        'words',
        type=str,
        help='The file name of a text file containing four letter words.'
    )
    parser.add_argument(
        'result_path',
        type=str,
        help='The file name of a text file that will contain the result.'
    )

    return parser.parse_args()
