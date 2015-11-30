# Exercise 12: Prompting People

# Variables
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

# Print
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


# Study Drills
#	1. In Terminal where you normally run python to run your scripts,
#	type pydoc raw_input. Read what it says. If you're on Windows
#	try python -m pydoc raw_input instead.
#	2. Get out of pydoc by typing q to quit.
#	3. Look onine for what the pydoc command does.
#	4. Use pydoc to also read about open, file, os and sys. It's
#	alright if you do not understand thosel just read through
#	and take notes about interesting things.

# Drill 1
#	Help on built-in function raw_input in module __builtin__:

#	raw_input(...)
#    	raw_input([prompt]) -> string
#    
#	Read a string from standard input.  The trailing newline is stripped.
#	If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#	On Unix, GNU readline is used if enabled.  The prompt string, if given,
#	is printed without a trailing newline before reading.
