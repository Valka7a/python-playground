# Exercise 24: More Practice

# Printing text and using tabs and new lines
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# Variable with tabs multyline comment and newlines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# Printing
print "--------------"
print poem
print "--------------"

# Variable with math and print it
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
# Create function to calculate and return result
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# variable and variables calling function
start_point = 10000
beans, jars, crates = secret_formula(start_point)
# Printing
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# Create variable
start_point = start_point / 10
# Printing
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


# Study Drills
#	1. Make sure to do your checks: read it backward, read it
#	out loud, and put comments above confusing parts.
#	2. Break the file on purpose, then run it to see what kinds
#	of errors you get. Make sure you can fix it.

# Drill 2 
# Traceback (most recent call last):
#  File "ex24.py", line 34, in <module>
#    print "With a starting point of: %d" % start_point
#NameError: name 'start_point' is not defined