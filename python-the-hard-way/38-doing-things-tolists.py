# Exercise 38: Doing Things to Lists

# How works append:
#	1. Python sees you mentioned 'mystuff' and looks up that variable.
#	It might have to look backward to see if you created with =, if it
#	is a function argument, or if it's a global variable. Either way it
#	has to find the 'mystuff' first.
#	2. Once it finds 'mystuff' it reads the '.'(period) operator and starts
#	to look at variables that are a part of 'mystuff'. Since 'mystuff' is a
#	list, it knows that 'mystuff' has a bunch of functions.
#	3. It then hits 'append' and compares the name to all the names that
#	'mystuff' says it owns. If 'append' is in there (it is) then Python
#	grabs that to use.
#	4. Next Python sees the '(' (parenthesis) and realizes, "Oh hey, this
#	should be a function". At this point it calls(runs, executes) the
#	function just like normally, but instead it calls the function with
#	an extra argument.
#	5. That extra argument is ... 'mystuff'! I know, weird, right? But that's
#	how Python works so it's best to just remember it and assume that's the
#	rusult. What happens, at the end of all this, is a function call that
#	look like: 'append(mystuff, 'hello')' instead of whay you read which
#	is 'mystuff.append('hello')'.

# Create varibale and print something
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."
# Create variable to split words in created variable
stuff = ten_things.split(' ')
# Create a list with new variables
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# Create while loop to get item by item from the list and store it in new
# variable and adding them in 'ten_things' while they get 10 stuffs
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."
# Print second word
print stuff[1]
# Print latest word
print stuff[-1] # whoa ! fancy
# Print what latest added
print stuff.pop()
# Print every word with space between them 
print ' '.join(stuff) # what? cool!
# Print Fourth element and fifth with '#' between them.
print '#'.join(stuff[3:5]) # super stellar!


# List Example:
#	1. You have a bunch of cards with values.
#	2. Those cards are in a stack, list or list from the top card to the
#	bottom card.
#	3. You can take cards off the top, the bottom, the middle at random.
#	4. If you want to find a specific card, you have to grab the deck and
#	go through it one at a time.

# Let's look at what i said:

#	"An ordered list"
#		Yes, deck of cards is in order with a first and a last.
#	"of things you want to store"
#		Yes, cards are things i want to store
#	"and access randomly"
#		Yes, i can grab a card from anywhere in the deck.
#	"or linearly"
#		Yes, if i want to find a specific card I can start at beginning
#		and go in order.
#	"by an index"
#		Almost, since with a deck of cards if I told you to get the card
#		at index 19 you'd have to count until you found that one. In our
#		Python lists the computer can just jump right to any index you
#		give it.
#
# That is all a list does, and this should give you a way to figure out
# concepts in programming. Every concept in programming usually has some
# relationship to the real world. At least the useful ones do. If you can
# figure out what the analog in the real world is, then you can use that 
# to figure out what the data structure should be able to do.


# When to Use Lists.

# You use a list whenever you have something that matches the list
# data structure's useful features:
#	1. If you need to maintain order. Remember, this is listed order,
#	not sorted order. Lists do not sort for you.
#	2. If you need to access the contents randomly by a number.
#	Remember, this is using cardinal numbers starting at 0.
# 	3. If you need to go through the contents linearly (first to last).
#	Remember, that's what 'for-loop' are for.




# Study Drills:
#	1. Take each function that is called, and go through the steps for
#	function calls to translate them to what Python does. For example,
#	'more_stuff.pop()' is 'pop(more_stuff)'.
#	2. Translate these two ways to view the function calls in English.
#	For example, 'more_stuff.pop()' reads as, "Call 'pop' with argument
#	'more_stuff'". Understand how they are really the same thing.
#	3. Go read about "object-oriented programming" online. Confused?
#	I was too. Do no worry. You will learn enough to be dangerous and
#	you can slowly learn more later.
#	4. Read up on what a "class" is in Python. Do not read about how
#	other languages use the word "class". That will only mess you up.
#	5. Do not worry if you do not have any idea what I'm talking about.
#	Programmers like to feel smart so they invented object-oriented
#	programming, named it OOP and then used it way too much. If you
#	think that's hard, you should try to use "functional programming".
#	6. Find 10 examples of things in the real world that would fit in 
#	a list. Try writing some scripts to work with them.

























































