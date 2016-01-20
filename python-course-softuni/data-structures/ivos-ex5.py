# Initial data
ivan_interests = [
    'пушене',
    'пиене',
    'тия три неща',
    'коли',
    'facebook',
    'игри',
    'разходки по плажа',
    'скандинавска поезия'
]

maria_interests = [
    'пиене',
    'мода',
    'facebook',
    'игри',
    'лов със соколи',
    'шопинг',
    'кино'
]

# Converting the lists into sets
ivan_interests_set = set(ivan_interests)
maria_interests_set = set(maria_interests)

# Print the intersection between the two sets
print(ivan_interests_set.intersection(maria_interests_set))
