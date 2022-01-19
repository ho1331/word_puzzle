from src.app import puzzle_length
from src.utils import get_parse_args


if __name__ == '__main__':
    args = get_parse_args()

    start_word = args.start
    end_word = args.end
    dict_file = args.words
    res_path = args.result_path

    puzzle_length(start_word, end_word, dict_file, res_path)
