# Exercise 39: Dictionaries, Oh Lovely Dictionaries

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


# Making Your Own Dictionary Modules:

# Files: 'hashmap.py' and 'ex39_text.py'



# The Code Description:

"""
This 'hashmap' is nothing more then "a list of buckets, which are a list
of slots, which have key/value pairs in them". Take a minute to break that
down to see what I mean:

	"a list of buckets..."
		In the 'hashmap' function I create the 'aMap' variable which is a 
		list and then I fill it with other lists..
	"which are a list of slots..."
		These bucket lists are empty at first, but as we add key/value pairs
		to the data structure they will fill with "slots" or..
	"which have key/value pairs in them."
		Meaning each slot inside a bucket contains a '(key, value)' tuple or
		"pair".

If this structure still doesn't make sense, take the time to draw it out on
paper until you're sure you get it. In fact, doing algorithms manually on 
paper is a good way to make sure you understand them.

Now that you know how the date is structured, you just need to know the 
algorithm for each operation. An algorithm is the steps you take to do something
to or with a data structure. It's the code that makes the data structure work.
We'll go through each of these operations using the code, but a general pattern
in the 'hashmap' algorithms is this:
	1. Convert a key to an integer using a hashing function: 'hash_key'.
	2. Convert this hash to a bucket number using a %(modulus) operator.
	3. Get his bucket from the 'aMap' list of buckets and then traverse it to
	find the slot that contains the key we want.

In the case of 'set' we do this, to replace duplicate keys or we append to add
new ones.

I will now walk through the code for the hashmap so you can understand what's 
going on, following function by function. Follow along and make sure you 
understand every line. Write an English comment above each line to make sure you
understand what it's doing. This is so deceptively simple that i recommend you
take the time to play with any lines of code mentioned in the following description
either in the Python shell or on paper until you get it.

	new
		First I start by creating a function that makes a hashmap for you, also 
		known as an initializer. What I've done is created an 'aMap' variable that
		has a list, and then I put 'num_buckets' lists inside it. These buckets will
		be used to hold he contents of the hashmap as I set them. Later I use 'len(aMap)'
		in other functions to find out how many buckets there are. Be sure you understand
		that!
	hash_key
		This deceptively simple function is the core of how a 'dict' works. What it
		does is uses the built-in Python 'hash' function to convert a string to a
		number. Python uses this function for its own 'dict' data structure and
		I'm just reusing it. You should fire up a Python console to see how it works.
		Once I have a number for the key, I then use the %(modulus) operator and the 
		'len(aMap)' to get a bucket where this key can go. As you should know, the %
		(modulus) operator will divide any number and give me the remainder. I can
		also use this as a way of limiting giant numbers to a fixe smaller set of 
		other numbers. If you don't get this then use Python to explore it.
	get_bucket
		This function then uses 'hash_key' to find the bucket that a key could be in.
		Since i did '% len(aMap)' in the 'hash_key' function, I know whatever 'bucket_id'
		I get will fit into the 'aMap' list. Using the 'bucket_id' I can then get the
		bucket where the key could be.
	get_slot
		This function uses 'get_bucket' to get the bucket a key could be in and then
		it simply rolls through every element of that bucket until it finds a matching
		key. Once it does it returns the tuple of '(i, k, v)' which is the indexthe key
		was found in, the key itself and the value set for that key. You now know enough
		to see how this data structure works. It takes keys, hashes and modulus them to
		find a bucket, then searches that bucket to find the item. This effectively cuts 
		the amount of searching necessary to a fraction of what it would be normally.
	get
		This is a "convenience function" which does what most people want a 'hashmap' to
		do. It uses 'get_slot' to get the '(i, k, v)' and then just returns the 'v(value)'
		only. Make sure you understand how the 'default' variable works and how the
		'(i, k, v)' in 'get_slot' is assigned to the 'i, k, v' variables in 'get'.
	set
		To set a key/value pair all I need to do is get the bucket and append the new
		'(key, value)' to it so it can be found later. However, I want my 'hashmap' to
		allow one key at a time. To do that, first I have to find the bucket then check
		if this key already exists. If it does then I replace it in the bucket with the
		new one and if it doesn't then I append. This is actually slower than simply 
		appending, but more likely what a user of 'hashmap' wants. If you wnated to allow
		multiple values for a key you could simply have 'get' go through every slot in the 
		bucket and return a list of everything it found. This is a good example of tradeoffs
		in design. The current version is faster on 'get', but slower on 'set'.
	delete
		To delete a key, I simply get the bucket and search for the key in it and delete it
		from the list. However, because I chose to make 'set' only store one key/value pair
		I can stop when I have found one. If I had decided to allow multiple values for each
		key by simply appending I would have also made 'delete' slower because I would have
		needed to go through every slot on delete just in case it had a key/value pair that matched.
	list
		The last function is simply a little debug function that prints out what's in the 
		'hashmap' and should be trivial for you to understand. It just gets each bucket,
		then goes through each slot in the bucket.

After all of these functions I just have a little bit of testing code that makes sure they work.
"""

# Three Levels of Lists
"""
As I mentioned in the descusiion, by deciding that 'set' will overwrite (replace)
keys with new values, I have made 'set' slowry but this assumption makes all of the 
other vuntions faser. What if I wanted a 'hashmap' that allowe multiple values for 
each key but still keep everything fast?

What I need to do then is establish that every slot in a bucket is a list of values.
This means that I add a third level of buckets, then slots, then values. This also
matches the description of this kind of 'hashmap' because I am saying, "For every key
there can be 'multiple' values." Another way to say that is "every key has a list of
values". Since keys go in slots, then slots have lists of values and I'm done.

If you want to take this code further, then change it to support multiple values for 
each key.
"""


# When to Use Dictionaries or Lists:
#	1. You have to retrieve things based on some identifier, like names,
#	addresses or anything that can be a key.
#	2. You don't need things to be in order. Dictionaries do not normally
#	have any notion of order, so you have to use a list for that.
#	You are going to be adding and removing elements and their keys.


# ******************************************************************************
# * This means that if you have to use a non-numeric key, use a 'dict'. If you *
# * need things in oredr, use a list. 										   *
# ******************************************************************************


# Study Drills:
#	1. Do this same kind of mapping with cities and states/regions in your
#	country or some other country.
#	2. Find the Python documentation for dictionaries and try to do even
#	more things to them.
#	3. Find out what you can't do with dictionaries. A big one is that they
#	do not have oredr, so try playing with that.
#	4. Read about Python's assert feature and then take the hashmap code
#	and add assertions for each of the tests I've done instead of print. For
#	exapmle, you can assert that the first get operation returns "Flamenco
#	Skatches" instead of just printing that out.
#	5. Did you notice that the 'list' function listed the items I added in
#	a different oredr that they were added? This is an example of how
#	dictionaries don't maintain order, and if you analyze the code you'll
#	understand why.
#	6. Create a 'dump' function that is like 'list' but which dumps the full
#	contents of every bucket so you can debug it.
#	7. Make sure you know what the 'has' function does in that code.
#	It's a special function that converts strings to a consistent integer.
#	Find the documentation for it online. Read about what a "hash function"
#	is in programming.


















































