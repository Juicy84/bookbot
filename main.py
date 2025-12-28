from stats import count_words
from stats import count_letters
from stats import char_count_sorted
from stats import list_to_dict
import sys

def get_book_text(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        content = get_book_text(sys.argv[1])
        word_count = count_words(content)

        letter_count = count_letters(content)
    #    print(letter_count)
        char_count_list = char_count_sorted(letter_count)
        letters_final = list_to_dict(char_count_list)
        print("============ BOOKBOT ============")
        print(f"Analysing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for key,num in letters_final.items():
            print(f"{key}: {num}")
        print("============= END ===============")

main()
