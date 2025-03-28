def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def count_words(text):
    word_list = text.split()
    return len(word_list)

def main():
    contents = get_book_text("books/frankenstein.txt")
    #print(get_book_text(contents)
    print(f"{count_words(contents)} words found in the document")
    return

main()
