from stats import word_count_from_text
from stats import character_count_from_text
from stats import sorter
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        book = file.read()
    return book


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_as_string = get_book_text(sys.argv[1])
    count = word_count_from_text(book_as_string)
    char_count = character_count_from_text(book_as_string)
    sorted_char_count = sorter(char_count)
    print("============ BOOKBOT ============"
          "\nAnalyzing book found at books/frankenstein.txt..."
          "\n----------- Word Count ----------"
          f"\nFound {count} total words"
          "\n--------- Character Count -------")
    for char, count in sorted_char_count:
        print(f"{char}: {count}")      
    print("\n============= END ===============")

    

main()