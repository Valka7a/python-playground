"""
words = ["apple", "bear", "cat", "doorknob", "elephant", "finger", "good"]
i trqq poluchish tova
[5, 8, 8, 6]
koeto e
dyljinata na vsichki dumi koito sa pone
5 simvola dylgi

polzvam filter + map
"""
words = ["apple", "bear", "cat", "doorknob", "elephant", "finger", "good"]

def get_len_words_in_list(list):
    thelen = filter(lambda word: len(word) >= 5, list)
    return map(lambda word: len(word), thelen)

print get_len_words_in_list(words)
