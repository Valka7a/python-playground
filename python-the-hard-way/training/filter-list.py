"""
sled nego.. imame slednoto
L = ["cat", "dogs", "card", "frogs", "finger"]
i trqbva da poluchish
3
koeto e broq na dumite koito imat dyljina koqto e chetna

trqbva da se kombinira
filter + reduce
"""

words = ["cat", "dogs", "card", "frogs", "finger"]

def words_left(list):
    return len(filter(lambda word: len(word) % 2 == 0, list))

print words_left(words)
