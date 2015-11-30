# Exercise 30: Else and If Statements

# Drill 2
people = 17
cars = 20
trucks = 35

# If cars are greater than people: prints..
if cars > people:
	print "We should take the cars."
# If cars less than people: prints..
elif cars < people:
	print "We should not take the cars."
# If both False: prints..
else:
	print "We can't decide."
# If trucks greater than cars: prints...
if trucks > cars:
	print "That's too many trucks."
# If trucks less than cars: prints...
elif trucks < cars:
	print "Maybe we could take the trucks."
# If both False: print...
else:
	print "We still can't decide."
# If people greater than trucks: prints..
if people > trucks:
	print "Alright, let's just take the trucks."
# If False: prints..
else:
	print "Fine, let's stay home then."



# Study Drills:
#	1. Try to guess what 'elif' and 'else' are doing.
#	2. Change the numbers of 'cars', 'people' and 'trucks' and then
#	trace through each 'if-statement' to see what will be printed.
#	3. Try some more complex boolean expressions like
#	'cars > people or trucks < cars'.
#	4. Above each line write an English description of what the line
#	does.


# Drill 1: 'elif' is one more stage to check, 
# if 'if' and 'elif' False then run 'else'

# Drill 3
# If cars less than people and trucks less than cars: prints...
if cars < people and trucks < cars:
	print "This is First."
# If people less than cars and trucks less then cars: prints...
elif people < cars and trucks < cars:
	print "This is Second."
# If trucks greater than cars or cars less then people: prints...
elif trucks > cars or cars < people:
	print "This is Third."
# If trucks equal to cars or cars equal to people: prints...
elif trucks == cars or cars == people:
	print "This is Fourth."
# If cars + trucks greather or equal people: prints...
elif cars + trucks >= people:
	print "This is Fifth."
# If all False: prints...
else:
	print "This is Final."