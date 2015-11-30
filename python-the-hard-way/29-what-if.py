# Exercise 29: What If Statement

people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

# Drill 5:
dogs += 6

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."



# Study Drills:
#	1. What do you think the 'if' does to the code under it?
#	2. Why does the code under the 'if' need to be indented
#	four spaces?
#	3. What happens if it isn't indented?
#	4. Can you put other boolean expressions from Exercise 27
#	in the 'if-statement'? Try it.
#	5. What happens if you change the initial values for
#	'people', 'cats' and 'dogs'?

# Drill 1: It's run the code below it if boolean expression is True

# Drill 2: Because the colon(:) of the end of line it the way how
# you telling python you are creating a new "block" of code and
# then the four spaces tells Python what lines of code are in
# that block, it's the same like functions.

# Drill 3: IndentationError: expected an indented block

# Drill 4:

if people + cats and not (cats == dogs):
	print "It's really bad."

if people != dogs:
	print "Someone will have more dogs or someone will haven't a dog."