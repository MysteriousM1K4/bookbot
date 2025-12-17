from stats import get_text_word_count, get_letter_count
import sys

def main():
    arguments = sys.argv
    if not len(arguments) > 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    data = get_book_text(arguments[1])
    print(f"============ BOOKBOT ============ \n Analyzing book found at {arguments[1]} \n ----------- Word Count ----------")
    print(f"Found {75767} total words")
    print("--------- Character Count -------")
    letter_count = get_letter_count(data)
    for key in letter_count:
        print(f"{key}: {letter_count[key]}")

def get_book_text(filepath):
    data = ""
    with open(filepath) as f:
        data = f.read()
    return data

main()