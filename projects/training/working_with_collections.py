animals = [
    {'name': 'Fluffykins',  'species': 'rabbit'},
    {'name': 'Caro',        'species': 'dog'},
    {'name': 'Hamilton',    'species': 'dog'},
    {'name': 'Harold',      'species': 'fish'},
    {'name': 'Ursula',      'species': 'cat'},
    {'name': 'Jimmy',       'species': 'fish'}
]


# Get dogs from list with dictionaries
def return_dogs(animals):
    dogs = []

    for animal in animals:
        if animal['species'] == 'dog':
            dogs.append(animal)
    return dogs

# Short way to get dogs
# Get only species equal to dog
def is_dog(animal):
    return animal['species'] == 'dog'


# Filter the list with 'is_dog' and return them
def filter_and_return(animals):
    return filter(is_dog, animals)


# Get names from list with dictionaries
def animal_names(animals):
    names = []

    for animal in animals:
        names.append(animal['name'])

    return names

# Short way to get names
# Get only names from dictionaries
def get_animal_name(animal):
    return animal['name']


def return_animal_name(animals):
    return map(get_animal_name, animals)


do = filter_and_return(animals)
print do

to = return_animal_name(animals)
print to



#dogs = return_dogs(animals)
#print dogs

#names = animal_names(animals)
#print names
"""
def animal_name(animals):
    return map(lambda animal: animal['name'], animals)

do = animal_name(animals)
print do

Notes:
Tova koeto pravq e da otdelq chast ot kolekciqta v nova -> filtiram
tova e edin pohvat ot fukncionalnoto programirane,
fuknciata 'filter'

NA EDNO
def get_dog_species(animals):
    dogs = filter(lamda a : a['species'] == 'dog', animals)
    return map(lambda d : d['species'], dogs)
"""
