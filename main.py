from stats import count_words, count_characters, dictsort
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()




def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    text = get_book_text(filepath)
    words = count_words(text)
    char_counts = dictsort(count_characters(text))

    print("========== BOOKBOT ==========")
    print(f"Analysing book found at {filepath}")
    print("---------- Word Count ----------")
    print(f"Found {words} total words")
    print("---------- Character Counts ----------")
    for item in char_counts:
        print(f"{item['char']}: {item['num']}")
    print("========== END ==========")
main()