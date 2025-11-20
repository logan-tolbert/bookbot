import sys
from stats import get_word_count, get_char_count, split_char_counts, print_report

def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print_report(sys.argv[1])
        sys.exit(0)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
