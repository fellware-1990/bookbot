from stats import word_count
from stats import character_count
from stats import sorted_list
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


path_to_book = sys.argv[1]


def main():
    book_path = path_to_book
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_count = character_count(text)
    char_list = sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_list:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        words = f.read()
        return words
    




main()  