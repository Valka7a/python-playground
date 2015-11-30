# Exercise 32: Loops and Lists

# How to make a lits:
hair = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
#---------------------------------
# Variable contain lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# For everything in variable do...
# This first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# For everything in variable do...
# Same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# For everything in variable do...
# Also we can go through mixed lists too.
# Notice we have to use %r since we don't know what's in it.
for i in change:
	print "I got %r" % i

# Make variable with empty list
# We can also build lists, first start with an empty one
elements = []

# For everything in range 0 to 6 do...
# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# Save everything in variable
	# Append is a function that lists understand
	elements.append(i)
	
# For everything in variable do...
# Now we can print them out too
for i in elements:
	print "Element was: %d" % i



# Study Drills:
#	1. Take a look at how you used 'range'. Look up the 'range' 
#	function to understand it.
#	2. Could you have avoided that 'for-loop' entirely on line
#	22 and just assigned 'range(0, 6)' directly to 'elements'?
#	3. Find the Python documentation on lists and read about
#	them. What other operations can you do to lists besides
#	'append'?

# No we can't, because of error.