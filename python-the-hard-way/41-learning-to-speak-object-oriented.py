# Exercise 41: Learning To Speak Object Oriented

# Word Drills:

"""
class: 
	Tell Python to make a new type of thing.
object: 
	Two meanings: the most basic type of thing and any instance of some thing.
instance: 
	What you get when you tell Python to create a class.
def: 
	How you define a function inside a class.
self: 
	Inside the functions in a class, self is a variable for the instance/object
	being accessed.
inheritance:
	The concept that one class can inherit traits from another class, much like
	you and your parents.
composition:
	The concept that a class can be composed of other classes as parts, much like
	how a car has wheels.
attribute:
	A property classes have that are from composition and are usually variables.
is-a:
	A phrase to say that something inherits from another, as in a "salmon" is-a "fish".
has-a:
	A phrase to say that something is composed of other things or has a trait, as in
	"a salmon has-a mouth".
"""


# Pharse Drills

"""
class X(Y)
	"Make a class named X that is-a Y."
class X(object): def __init__(self, J)
	"class X has-a __init__ that takes self and J parameters."
class X(object): def M(self, J)
	"class X has-a function named M that takes self and J parameters."
foo = X()
	"Set foo to an instance of class X."
foo.M(J)
	"From foo get the M function and call it with parameters self, J."
foo.K = Q
	"From foo get the K attribute and set it to Q."

In each of these where you see X, Y, M, J, K, Q and foo you can treat those like
blank spots. For example, I can also write these sentences as follows:
	1. "Make a class named ??? that is-a Y."
	2. "class ??? has-a __init__ that takes self and ??? parameters."
	3. "class ??? has-a function named ??? that takes self and ??? parameters."
	4. "Set foo to an instance of class ???."
	5. "From foo get the ??? function and call it with self=??? and parameters ???."
	6. "From foo get the ??? attribute and set it to ???."

"""

# Combined Drills
#	1. Take a pharse card and drill it.
#	2. Flip it over and read the sentence and for each word in the sentence
#	that is in your words drills, get that card.
#	3. Drill those words for that sentence.
#	4. Keep going until you are bored, then take a break and do it again.



# A Reading Test
# oop_test.py run with english


# Reading More Code:
#	1. For each class give its name and what other classes it inherits from.
#	2. Under that, list every function it has and the parameters they take.
#	3. List all of the attributes it uses on its self.
#	4. For each attribute, give the class this attribute is.
