# Exercise 20: Functions and Files
# Import
from sys import argv

script, input_file = argv
# Function to print a file
def print_all(f):
    print f.read()
# Function to set position at the offset
def rewind(f):
    f.seek(0)
# Function to count lines and read them
def print_a_line(line_count, f):
    print line_count, f.readline()
# Open file
current_file = open(input_file)

print "First let's print the whole file:\n"
# Call function to print all the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# Change position at the offset
rewind(current_file)

print "Let's print three lines:"
# Variable for line and call function to print the line
current_line = 1
print_a_line(current_line, current_file)
# Variable for next line and call function to print the line
# Drill 5
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# Variable for next line and call function to print the line
# Drill 5
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# Study Drills
#	1. Write English comments for each line to understand what
#	that line does.
#	2. Each time 'print_a_line' is run, you are passing in a
#	variable 'current_line'. Write out what 'current_line' is
#	equal to on each function call, and trace how it becomes
#	'line_count' in 'print_a_line'.
#	3. Find each place a function is used, and check its 'def'
#	to make sure that you are giving it the right arguments.
#	4. Research onine what the 'seek' function for 'file' does.
#	Try 'pydoc file' and see if you can figure it out from there.
#	5. Research the shorthand notation += and rewrite the script
#	to use += instead. 