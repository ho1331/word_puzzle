import argparse
import os
import json


def words_reader(filename):
    """
    Read data from file.

    Args:
        filename (str): the file name of a text file

    Returns:
        list: list with some data
    """
    file = os.path.abspath(filename)
    with open(file, 'r') as file:
        data = json.loads(file.read())

    return data


def steps_writter(words, path):
    """
    Write data into txt file.

    Args:
        words (list): list of four letter words
        path (str): the path to some directory
    """
    with open(f'{path}/result.txt', 'w+') as file:
        file.write(','.join(words))


def get_parse_args():
    """
    Parses command line arguments.

    Returns:
        [method]: parse_args() method of argparse.ArgumentParser class
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
