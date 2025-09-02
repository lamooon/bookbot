from stats import get_num_words
from stats import char_appearance
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        print(file_contents)


def sort_on(appearance):
    return appearance["num"]


def main():
    char_count = char_appearance(sys.argv[1])
    char_count_to_list = [{"char": k, "num": v} for k, v in char_count.items()]
    char_count_to_list.sort(reverse=True, key=sort_on)
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------""")

    print(f"Found {get_num_words(sys.argv[1])} total words")
    print("--------- Character Count -------")
    for char in char_count_to_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")


main()
