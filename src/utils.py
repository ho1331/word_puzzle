import argparse
import json
import os
import logging
import logging.config


LOG_FILENAME = os.path.join(os.getcwd(), "app.log")

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d]: %(message)s'
        },
    },

    'handlers': {
        'default': {
            'filename': LOG_FILENAME,
            'class': 'logging.FileHandler',
            'formatter': 'default_formatter',
        },
    },

    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def words_reader(filename):
    """
    Read data from file.

    Args:
        filename (str): the file name of a text file

    Returns:
        list: list with some data
    """
    path = os.path.abspath(filename)

    try:
        with open(path, 'r') as file:
            data = json.loads(file.read())
    except FileNotFoundError as exp:
        logger.exception(exp)
        raise

    return data


def steps_writer(words, path):
    """
    Write data into txt file.

    Args:
        words (list): list of four letter words
        path (str): the path to some directory
    """
    try:
        with open(f'{path}/result.txt', 'w+') as file:
            file.write(','.join(words))
    except FileNotFoundError as exp:
        logger.exception(exp)
        raise


def checker_word(word):
    """
    Args:
        word (sys.argv): 4-letters word

    Raises:
        argparse.ArgumentTypeError: if the word length is not equal to 4

    Returns:
        str: 4-letters word
    """
    if len(word) == 4:
        return word
    else:
        raise argparse.ArgumentTypeError('The word must be 4-letters')


def checker_path(path):
    """
    Args:
        path (sys.argv): path to data store

    Raises:
        argparse.ArgumentTypeError: if the path doesn't exist

    Returns:
        str: path to the data store
    """
    if os.path.exists(os.path.join(os.getcwd(), path)):
        return path
    else:
        raise argparse.ArgumentTypeError(f'No such file or directory: {path}')


def get_parse_args():
    """
    Parses command line arguments.

    Returns:
        [method]: parse_args() method of argparse.ArgumentParser class
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'start',
        type=checker_word,
        help='The start word.'
    )
    parser.add_argument(
        'end',
        type=checker_word,
        help='The end word.'
    )
    parser.add_argument(
        'words',
        type=checker_path,
        help='The file name of a text file containing four letter words.'
    )
    parser.add_argument(
        'result_path',
        type=checker_path,
        help='The file name of a text file that will contain the result.'
    )

    return parser.parse_args()
