# Rabotqt samo sus list
# The list
"""
animals = [
    {'name': 'Fluffykins',  'species': 'rabbit'},
    {'name': 'Caro',        'species': 'dog'},
    {'name': 'Hamilton',    'species': 'dog'},
    {'name': 'Harold',      'species': 'fish'},
    {'name': 'Ursula',      'species': 'cat'},
    {'name': 'Jimmy',       'species': 'fish'}
]
"""
# Filter discription
"""
def is_dog(animal):
    return animal['species'] == 'dog'

def filter_and_return(animals):
    return filter(is_dog, animals)


Filter-a raboti po sledniq imash filter(test_function, list) taq test_function
se prilaga za vseki element ot lista i zaduljitelno trqbva da vrushta bool(==,<=)
ako e true otiva vyv noviq list ako ne go podminava. Filtera sledva uslovieto na
test_function vuv list. Filter-a kakto mu e imeto toi filtrira rezultati bazirano
na test_function sreshtu vseki element ot lista koito si mu dal, ako minat testa
minavat v noviq masiv, ako ne se ignorirat.

Naricha se higher order function koeto shte reche funkciq koqto priema druga
funkciq kato argument ili vryshta funkciq.
Znachi az mu kazvam da filtrira lista sledvaiki test_fuknction
da tochno a test function-a zadyljitelno trqbva da vyrn e bool(==) rezultat v
sluchaq animal['species'] == 'dog' ti vryshta true ili false drugoto koeto e
test function-a vinagi priema kato argument.
Elementa ot spisyka koito e v momenta dokyto iterira prez vsichki toest tq se
pylni sys vseki edin element i go probva dokyot ne minat vsichki.
Tova koeto pravish v cikyla e syshtoto realno samo deto ne apply-vash funciq
ami direktno si proverqvash i pravish nov masiv ama realno taka trqbva da se
pishe a ne s for cikli.
"""

# QUESTION
a v drugiq example
zashto polzvame map a ne pak filter?

# Map description
"""
def get_animal_name(animal):
    return animal['name']

def return_animal_name(animals):
    return map(get_animal_name, animals)


Ideqta na map-a pyk e da transformira daden list v nov list bazirano na nqkva
funkciq koqto transformira elementite edin po edin.
map(get_animal_name, animals)
V sluchaq vurpi po elemenite v animals po uslovieto na get_animal_name i tursi
'name' kato sybira texnata stoinost vuv nov list
"""


# Lambda description
"""
V toq primer filter(lambda a : a['species'] == 'dog', animals)
realno pravish vse 1 si podal lambda(a): return a['species'] == 'dog'
Lambda e anonimna fuknciq.
ako ti trqbva... ! po-slojna logika togava ne se polzva lamda
"""


# Reduce description
"""
reduce(lambda total, order: order['amount'] + total, orders, 0)

ideqta e slednata: imash list, koito trqbva ot nego da generirash 1 value i
reduce ti pomaga da go napravish v sluchaq e sum.
inache imam

reduce(nqkyv_function_per_item, list_of_items, inital_value)
"""
