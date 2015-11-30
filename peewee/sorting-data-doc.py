"""
Let's begin by populating the database with some people. We will use the 'save()'
and 'create()' methods to add and update people's records.
________________________________________________________________________________
>>> from datetime import date
>>> uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
>>> uncle_bob.save() # bob is now stored in the database
1
________________________________________________________________________________

________________________________________________________________________________
    !Note
When you call 'save()', the number of rows modified is returned.
________________________________________________________________________________

You can also add a person by calling the 'create()' method, which returns a model
instace:
________________________________________________________________________________
>>> grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
>>> herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
________________________________________________________________________________

To update a row, modify the model instance and call 'save()' to persist the changes.
Here we will change Grandma's name and then save the changes in the database:
________________________________________________________________________________
>>> grandma.name = 'Grandma L.'
>>> grandma.save() # Update grandma's name in the database.
1
________________________________________________________________________________

Now we have stored 3 people in the database. Let's give them some pets. Grandma
doesn't like animals in the house, so she woun't have any, but Herb is an animal lover:
________________________________________________________________________________
>>> bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
>>> herb_fibo = Pet.create(owner=herb, name='Fido', animal_type='dog')
>>> herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
>>> herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
________________________________________________________________________________

After a long full life, Mittens sicknes and dies. We need to remove him from the
database:
________________________________________________________________________________
>>> herb_mittens.delete_instance() # he had a great life
1
________________________________________________________________________________


________________________________________________________________________________
    !Note
The return value of 'delete_instance()' is the number of rows removed from the
database.
________________________________________________________________________________

Uncle Bob decides that too many animals have been dying at Herb's house, so he
adopts Fido:
________________________________________________________________________________
>>> herb_fido.owner = uncle_bob
>>> herb_fido.save()
>>> bob_fido = herb_fido # rename our variable for clarity
________________________________________________________________________________
