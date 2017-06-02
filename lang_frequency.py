#!/usr/bin/python3

import sys
import re
from collections import Counter

number_of_top_words = 10


def load_words_from_text_file(filename: "str") -> "iter":
    with open(filename, 'r', encoding='utf-8') as f:
        raw_text = f.read().lower()
    return filter(len, [word for word in re.split('[^a-z]', raw_text)])


def get_most_frequent_words(words: "iter") -> "list":
    text_dict = Counter(words)
    return text_dict.most_common(number_of_top_words)


def main(filename):
    words = load_words_from_text_file(filename)
    print(*get_most_frequent_words(words))


if __name__ == '__main__':
    main(sys.argv[1:][0])
