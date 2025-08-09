#!/usr/bin/env python3

import sys
from stats import count_words
from stats import get_char_frequency
from stats import count_chars

def main():

    if len(sys.argv) < 2:
        usage()

    filepath=sys.argv[1]
    
    text = get_book_text(filepath)
    wc = count_words(text)
    cc = count_chars(text)

    # print(f"{wc} words found in the document")
    # print(get_char_frequency(text))

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print(f"----------- Word Count ----------")
    print(f"Found {wc} total words")

    print(f"--------- Character Count -------")
    for c in cc:
        print(f"{c['char']}: {c['count']}")

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
