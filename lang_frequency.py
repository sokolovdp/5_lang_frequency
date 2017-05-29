#!/usr/bin/python3
# -*- coding: utf-8

import sys
import re
from collections import Counter


def load_data(filename: "str") -> "list":
    with open(filename, 'r', encoding='utf-8') as f:
        raw_text = f.read().lower()
    return [word for word in re.split('[^a-z]', raw_text) if word]


def get_most_frequent_words(words: "list") -> "list":
    text_dict = Counter(words)
    return [key for key in sorted(text_dict, key=text_dict.get, reverse=True)][:10]


def main(filename):
    words = load_data(filename)
    print(', '.join(get_most_frequent_words(words)))


if __name__ == '__main__':
    main(sys.argv[1:][0])
