def count_words(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    glyphs = set()
    counts = {}
    for s in text:
        glyphs.add(s.lower())
    print(glyphs)
    for g in glyphs:
        counts[g] = 0
        #print(glyphs)
    for s in text:
        for g in glyphs:
            if s.lower() == g:
                counts[g] += 1







    return counts