# Exercise 40: Modules, Classes and Objects

# Modules Are Like Dictionaries
import mystuff

#	mystuff = {'apple': "I AM APPLES!"}
#	print mystuff


# Keep this idea of "get X from Y" in your head and now think about modules.
# You've made a few so far and you should know they are:
#	1. A Python file with some functions or variables in it ..
#	2. You import that file.
#	3. And you can access the function or variables in that module with the
#	'.'(dot) operator.


#	mystuff.apple()
#	print mystuff.tangerine

# It's similar like to use dictinary but different syntax:

# mystuff['apple'] 		get apple from dict
# mystuff.apple() 	 	get apple from the module
# mystuff.tangerine 	same thing, it's just a variable

# This means we have a very common pattern in Python:
#	1. Take a key=value style container.
#	2. Get something out of it by the key's name.

# In the case of the dictionary, the key is a string and the syntax is '[key]'.
# In the case of the module, the key is an indentifier and the syntax is '.key'.
# Other than that they are nearly the same thing.



# Classes Are Like Modules
# If I were to create a class just like the 'mystuff' module, I'd do something
# like this:

class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

		def apple(self):
			print "I AM CLASSY APPLES!"


# Objects are Like Import

# You instantiate(create) a class by calling the class like it's a function, like this:
# thing = MyStuff()
# thing.apple()
# print thing.tangerine

# The first line is the "instantiate" operation and it's a lot like calling a function.
# However, Python coordinates a sequence of events for you behind the scenes. I'll go
# through these steps using the above code for 'MyStuff':
#	1. Python looks for 'MyStuff()' and sees that it is a class you've defined.
#	2. Python crafts an empty object with all the functions you've specified in the
#	class using 'def'.
#	3. Python then looks to see if you made a "magic" '__init__' function and if you
#	have it calls that function to initialize your newly created empty object.
#	4. In the 'MyStuff' function '__init__' I then get this extra variable 'self',
#	which is that empty object Python made for me and I can set variables on it
#	just like you would with a module, dictionary or other object.
#	5. In this case, I set 'self.tangerine' to a song lyric and then i've initialized
#	this object.
#	6. Now Python can take this newly minted object and assign it to the 'thing'
#	variable for me to work with.

# **************************************************************************
# Classes are like blueprints or definitions for creating new mini-modules.
# Instantiation is how you make one of these mini-modules and import it at
# the same time. "Instantiate" just means to create an object from the class.
# The resulting created mini-module is called an object and you then assign
# it to a variable to work with it.
# **************************************************************************



# Getting Things from Things

# dict style
# 	mystuff['apples']

# module style
# 	mystuff.apples()
#	print mystuff.tangerine

# class style
#	thing = MyStuff()
#	thing.apples()
#	print thing.tangerine


# A First Class Example

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

lovely_song = Song(["This is my first song",
					"And It's for my baby",
					"I love you my sunshine!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

lovely_song.sing_me_a_song()

# Study Drills:
#	1. Write some more songs using this and make sure you understand that you're
#	passing a list of strings as the lyrics.
#	2. Put the lyrics in a separate variable, then pass that variable to the class
#	to use instead.
#	3. See if you can hack on this and make it do more things. Don't worry if you
#	have no idea how, just give it a try and see what happens. Break it, trash it,
#	thrash it, you can't hurt it.
#	4. Search online for "object-oriented programming" and try to overflow your
#	brain with what you read. Don't worry if it makes absolutely no sense to you.
#	Half of that stuff makes no sense to me too.










































