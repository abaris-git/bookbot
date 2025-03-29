def count_words(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    glyphs = set()
    counts = {}
    for s in text:
        glyphs.add(s.lower())
    for g in glyphs:
        counts[g] = 0
    for s in text:
        for g in glyphs:
            if s.lower() == g:
                counts[g] += 1

    return counts


def char_sort_to_list(chars):
    char_list = []
    for char in chars:
        dictionary = {}
        dictionary["symbol"] = char
        dictionary["quant"] = chars[char]
       # print(dictionary)
        char_list.append(dictionary)
    #char_list.sort(key=sort_to)

    return char_list