# Exercise 13: Parameters, Unpacking, Variables

# Import
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Study Drills
#	1. Try giving fewer than three arguments to your script. See
#	that error you get? See if you can explain it.
#	2. Write a script that has fewer arguments and one that has 
#	more. Make sure you give the unpacked variables good names.
#	3. Combine raw_input with argv to make a script that gets 
#	more input from a user.
#	4. Remember that modules give you features. Modules.
#	Modules. Remember this because we'll need it later.


# Drill 3

# Make variable with raw_input
fourth = raw_input("Input fourth variable. ")
five = raw_input(third)

# Combine it with argv
print "Script: %r, First: %r, Second: %r, Third: %r, Fourth: %r and Five: %r." % (script, first, second, third, fourth, five)