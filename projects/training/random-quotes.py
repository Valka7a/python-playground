import random

quotes = ["noun is not a noun to be verb but a noun to be verb",
        "noun are about what verb can verb and what adjectives can verb",
        "adjectives looking for adjectives while verb and verb about noun and noun"]
nouns = ["mom", "dad", "John", "bike", "ball", "car", "door", "dog", "cat", "lion"]
verbs = ["run", "play", "swim", "fly", "drive", "eat", "talk", "drink", "walk"]
adjectives = ["wooden", "american", "bulgarian", "beautiful", "breakable", "homeless"]



def split_quote(quotes):
    quote = random.choice(quotes)
    return quote.split()


def find_and_replace(quotes):
    quotes = split_quote(quotes)
    for index, word in enumerate(quotes):
        if word == "noun":
            quotes[index] = random.choice(nouns)
        elif word == "verb":
            quotes[index] = random.choice(verbs)
        elif word == "adjectives":
            quotes[index] = random.choice(adjectives)
    return quotes


def print_random_quote(quotes):
    quote = find_and_replace(quotes)
    print ' '.join(quote)

print_random_quote(quotes)
