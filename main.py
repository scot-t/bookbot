#!/usr/bin/env python3

import sys
from stats import (
        get_num_words,
        get_num_chars
        )

def main():

    if len(sys.argv) < 2:
        usage()
    filepath=sys.argv[1]
    
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)

    print_report(filepath, num_words, num_chars)


def print_report(filepath, wc, cc):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print(f"----------- Word Count ----------")
    print(f"Found {wc} total words")

    print(f"--------- Character Count -------")
    for c in cc:
        if not c["char"].isalpha():
            continue
        print(f"{c['char']}: {c['num']}")

    print(f"============= END ===============")


def get_book_text(filepath):
    """
    Returns the contexnts of the file at filepath as string
    """
    with open(filepath) as f:
        text = f.read()
    return text


def usage():
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)


main()
