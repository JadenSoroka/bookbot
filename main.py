from stats import get_word_count, get_character_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        word_count = get_word_count(sys.argv[1])
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        get_character_count(sys.argv[1])

main()