"""
The real strength of our database is in how it allows us to retrieve data through
queries. Relational databases are excellent for making ad-hoc queries.
"""

# Getting single records
"""
Let's retrieve Grandma's record from the database. to get a single record from the
database, use 'SelectQuery.get()':
________________________________________________________________________________
>>> grandma = Person.select().where(Person.name == 'Grandma L.').get()
________________________________________________________________________________

We can also use the equivalent shorthand 'Model.get()':
________________________________________________________________________________
>>> grandma = Person.get(Person.name == 'Grandma L.')
________________________________________________________________________________
"""

# Lists of records
"""
Let's list all the people in the database:
________________________________________________________________________________
>>> for person in Person.select():
...     print person.name, person.is_relative
...
Bob True
Grandma L. True
Herb False
________________________________________________________________________________

Let's list all the cats and their owner's name:
________________________________________________________________________________
>>> query = Pet.select().where(Pet.animal_type == 'cat')
>>> for pet in query:
...     print pet.name, pet.owner.name
...
Kitty Bob
Mittens Jr Herb
________________________________________________________________________________

There is a big problem with the previous query: because we are accessing 'pet.owner.name'
and we did not select this value in our original query, peewee will have to perform
an additional query to retrieve the pet's owner. This behavior is referred to as
N+1 and it should generally be avoided.

We can avoid the extra queries by selecting both Pet and Person, and adding a join.
________________________________________________________________________________
>>> query = (Pet
...             .select(Pet, Person)
...             .join(Person)
...             .where(Pet.animal_type =='cat'))
...
Kitty Bob
Mittens Jr Herb
________________________________________________________________________________

Let's get all the pets owned by Bob:
________________________________________________________________________________
>>> for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
...     print pet.name
...
Kitty
Fido
________________________________________________________________________________

We can do another cool thing here to get bob's pets. Since we already have an object
to represent Bob, we can do this instead:
________________________________________________________________________________
>>> for pet in Pet.select().where(Pet.owner == uncle_bob):
...     print pet.name
...
Kitty
Fido
________________________________________________________________________________

Let's make sure these are sorted alphabetically by adding an order_by() clause:
________________________________________________________________________________
>>> for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
...     print pet.name
...
Fido
Kitty
________________________________________________________________________________

Let's list all the people now, youngest to oldest:
________________________________________________________________________________
>>> for person in Person.select().order_by(Person.birthday.desc()):
...     print person.name, person.birthday
...
Bob 1960-01-15
Herb 1950-05-05
Grandma L. 1935-03-01
________________________________________________________________________________

Now let's list all the people and some info about their pets:
________________________________________________________________________________
>>> for person in Person.select():
...     print person.name, person.pets.count(), 'pets'
...     for pet in person.pets:
...         print '    ', pet.name, pet.animal_type
...
Bob 2 pets
    Kitty cat
    Fido dog
Grandma L. 0 pets
Herb 1 pets
    Mittens Jr cat
________________________________________________________________________________

Once again we've run into a classic example of N+1 query behavior. We can avoid this
by performing a JOIN and aggregating the records:
________________________________________________________________________________
>>> subquery = Pet.select(fn.COUNT(Pet.id)).where(Pet.owner == Person.id)
>>> query = (Person
...             .select(Person, Pet, subquery.alias('pet_count'))
...             .join(Pet, JOIN.LEFT_OUTER)
...             .order_by(Person.name))

>>> for person in query.aggregate_rows():   # Note the 'aggregate_rows()' call.
...     print person.name, person.pet_count, 'pets'
...     for pet in person.pets:
...         print '    '.pet.name, pet._animal_type
...
Bob 2 pets
    Kitty cat
    Fido dog
Grandma L. 0 pets
Herb 1 pets
    Mittens Jr car
________________________________________________________________________________

Even though we created the subquery separately, only one query is actually executed.

Finnaly, let's do a complicated one. Let's get all the people whose birthday was
either:

    * before 1940(grandma)
    * after 1959(bob)
________________________________________________________________________________
>>> d1940 = date(1940, 1, 1)
>>> d1960 = date(1960, 1, 1)
>>> query = (Person
...             .select()
...             .where((Person.birthday < d1940 | (Person.birthday > d1960))))
...
>>> for person in query:
...     print person.name, person.birthday
...
Bob 1960-01-15
Grandma L. 1935-03-01
________________________________________________________________________________

Now let's do the opposite. People whose birthday is between 1940 and 1960:
________________________________________________________________________________
>>> query = (Person
...             .select()
...             .where((Person.birthday > d1940) & (Personal.birthday < d1960)))
...
>>> for person in query:
...     print person.name, person.birthday
...
Herb 1950-05-05
________________________________________________________________________________

One last query. This will use a SQL function to find all people whose names start
with either or lower-case G:
________________________________________________________________________________
>>> expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'g')
>>> for person in Person.select().where(expression):
...     print person.name
...
Grandma L.
________________________________________________________________________________

We're done with our database, let's close the connection:
________________________________________________________________________________
>>> db.close()
________________________________________________________________________________

This is just the basics! You can make your queries as complex as you like.

All the other SQL clauses are available as well, such as:
    * group_by()
    * having()
    * limit() and offset()

Check the documentation on Querying for more info.
"""
