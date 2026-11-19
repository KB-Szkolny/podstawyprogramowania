# Moduł MyText dla zadania 3-23
def word_count(text):
    return len(text.split())

def words_by_length_desc(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def words_alphabetically(text):
    words = text.split()
    return sorted(words)