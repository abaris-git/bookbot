from stats import count_words
from stats import char_count

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents


def main():
    contents = get_book_text("books/frankenstein.txt")
    #print(get_book_text(contents)
    print(f"{count_words(contents)} words found in the document")
    print(char_count(contents))
    return

main()
