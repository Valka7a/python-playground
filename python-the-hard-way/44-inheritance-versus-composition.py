# Exercise 44: Inheritance Versus Composition

# What is Inheritance?
"""
Inheritance is used to indicate that one class will get most or all of its 
features from a parent class. This happens implicitly whenever you write 
class Foo(Bar), which says "Make a class Foo that inherits from Bar." When 
you do this, the language makes any action that you do on instances of Foo 
also work as if they were done to an instance of Bar. Doing this lets you 
put common functionality in the Bar class, then specialize that functionality 
in the Foo class as needed.

When you are doing this kind of specialization, there are three ways that 
the parent and child classes can interact:
	1. Actions on the child imply an action on the parent.
	2. Actions on the child override the action on the parent.
	3. Actions on the child alter the action on the parent.

I will now demonstrate each of these in order and show you code for them.
"""

# Implicit Inheritance

# First I will show you the implicit actions that happen when you define a function
# in the parent, but not in the child.

class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

"""
The use of pass under the class Child: is how you tell Python that you want an 
empty block. This creates a class named Child but says that there's nothing new 
to define in it. Instead it will inherit all of its behavior from Parent. When 
you run this code you get the following:

$ python ex44a.python
PARENT implicit()
PARENT implicit()

Notice how even though I'm calling son.implicit() on line 16, and even though 
Child does not have a implicit function defined, it still works and it calls 
the one defined in Parent. This shows you that, if you put functions in a base 
class (i.e., Parent) then all subclasses (i.e., Child) will automatically get 
those features. Very handy for repetitive code you need in many classes.
"""


# Override Explicitly

class Parent(object):

	def override(self):
		print "PARENT override()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

"""
In this example I have a function named override in both classes, so let's see 
what happens when you run it.

$ python ex44b.py
PARENT override()
CHILD override()


As you can see, when line 14 runs, it runs the Parent.override function because 
that variable (dad) is a Parent. But when line 15 runs it prints out the 
Child.override messages because son is an instance of Child and Child overrides 
that function by defining its own version.

Take a break right now and try playing with these two concepts before continuing.
"""

# Alter Before or After

"""
The third way to use inheritance is a special case of overriding where you want 
to alter the behavior before or after the Parent class's version runs. You first 
override the function just like in the last example, but then you use a Python 
built-in function named super to get the Parent version to call. Here's the 
example of doing that so you can make sense of this description:
"""
print "\n\n"

class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

""" 
The important lines here are 9-11, where in the Child I do the following when
son.altered() is called:
	1. Because I've overridden Parent.altered the Child.altered version runs
	and line 9 executes like you'd expect.
	2. In this case I want to do a before and after so after line 9, I want to
	use super to get the Parent.altered version.
	3. On line 10 I call super(Child, self).altered(), which is aware of 
	inheritance and will get the Parent class for you. You should be able to 
	read this as "call super with arguments Child and self, then call the function
	altered on whatever it returns".
	4. At this point, the Parent.altered version of the function runs and that prints
	out the Parent message.
	5. Finally, this returns from the Parent.altered and the Child.altered function
	continues to print out the after message.


"""


# All Three Combined
"""
To demonstrate all of these, I have a final version that shows each kind of 
interaction from inheritance in one file:
"""
print "\n\n"

# create parent class
class Parent(object):
# def parent methods to print something
	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

# create class that inheritance Parent class
class Child(Parent):
# ovverride methon from parent to print something else	
	def override(self):
		print "CHILD override()"
# ovverride methon from parent to print something, then print the parent method
# using super() and then continue with print something else.
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
# create an instance of parent and child
dad = Parent()
son = Child()
# call the instance with implicit() method
dad.implicit()
son.implicit()
print "\n"
# call the instance with ovverride() method
dad.override()
son.override()
print "\n"
# call the instance with altered() method
dad.altered()
son.altered()


# The Reason for super()
"""
This should seem like common sense, but then we get into trouble with a thing 
called multiple inheritance. Multiple inheritance is when you define a class 
that inherits from one or more classes, like this:

class SuperFun(Child, BadStuff):
	pass

This is like saying, "Make a class named SuperFun that inherits from the classes 
Child and BadStuff at the same time."

In this case, whenever you have implicit actions on any SuperFun instance, Python 
has to look-up the possible function in the class hierarchy for both Child and 
BadStuff, but it needs to do this in a consistent order. To do this Python uses 
"method resolution order" (MRO) and an algorithm called C3 to get it straight.

Because the MRO is complex and a well-defined algorithm is used, Python can't 
leave it to you to get the MRO right. Instead, Python gives you the super() 
function, which handles all of this for you in the places that you need the 
altering type of actions as I did in Child.altered. With super() you don't have 
to worry about getting this right, and Python will find the right function for you.
"""


# Using super() with __init__
"""
The most common use of super() is actually in __init__ functions in base classes.
This is usually the only place where you need to do some things in a child, then
complete the initialization in the parent. Here's a quick example fo doing that
in the Child:

class Child(Parent):

	def __init__(self, stuff):
		self.stuff = stuff
		super(Child, self).__init__()


This is pretty much the same as the Child.altered example above, except I'm
setting some variables in the __init__ before having the Parent initialize with
its Parent.__init__.
"""

# Composition
"""
Inheritance is useful, but another way to do the exact same thing is just to use
other classes and modules, rather than rely on implicit inheritance. If you at
the three ways to exploit inheritance, two of the three involve writing new code
to replace or alter functionality. This can easily be replicated by just calling 
functions in a module. Here's an example of doing this:
"""

class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()
print "\n"
son.implicit()
print "\n"
son.override()
print "\n"
son.altered()

"""
In this code I'm using the name Parent, since there is not a parent-child is-a
relationship. This is a has-a relationship, where Child has-a Other that it uses
to get its work done. When I run this I get the following output:

$ python ex44e.py
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()

You can see that most of the code in Child and Other is the same to accomplish the
same thing. The only difference is that i had to define a Child.implicit function to
do that one action. I could then ask myself if I need this Other to be a class and
could I just make it into a module named other.py?
"""

# When to Use Inheritance or Composition
"""
The question of "inheritance versus composition" comes down to an attempt to solve the
problem of reusable code. You don't want to have duplicated code all over your software, 
since that's not clean and efficient. Inheritance solves this problem by creating a 
mechanism for you to have implied features in base classes. Composition solves this by 
giving you modules and the ability to call functions in other classes.

If both solutions solve the problem of reuse, then which one is appropriate in which
situations? The answer is incredibly subjective, but I'll give you my three guidelines 
for when to do which:

	1. Avoid multiple inheritance at all costs, as it's too complex to be reliable.
	If you're stuck with it, then be prepared to know the class hierarchy and spend
	time to finding where everything is coming from.
	2. Use composition to package code into modules that are used in many different
	unrelated places and situations.
	3. Use inheritance only when there are clearly related reusable pieces of code 
	that fit under a single common concept or if you have to because of something 
	you're using.

Do not be a slave to these rules. The thing to remember about object-oriented-
programming is that it is entirely a social convention programmers have created to 
package and share code. Because it's a social convention, but one that's codified in
Python, you may be forced to avoid these rules because of the people you work with.
In that case, find out how they using things and then just adapt to the situation.
"""

# Study Drills:
"""
There is only one Study Drill for this exercise because it is a big exercise. Go and 
read http://www.python.org/dev/peps/pep-0008/ and start trying to use it in your code. 
You'll notice that some of it is different from what you've been learning in this book, 
but now you should be able to understand their recommendations and use them in your own 
code. The rest of the code in this book may or may not follow these guidelines depending 
on if it makes the code more confusing. I suggest you also do this, as comprehension is 
more important than impressing everyone with you knowledge of esoteric style rules.
"""





€€
































