from stats import count_words
from stats import char_count
from stats import char_sort_to_list

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents


def main():
    book = "books/frankenstein.txt"
    contents = get_book_text(book)
    char_totals = char_count(contents)
    char_list = char_sort_to_list(char_totals)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(contents)} total words")
    print("--------- Character Count -------")
    for char in char_list:
        if char["symbol"].isalpha():
            letter = char["symbol"]
            value = char["quant"]
            print(f"{letter}: {value}")
    print("============= END ===============")
    return

main()
