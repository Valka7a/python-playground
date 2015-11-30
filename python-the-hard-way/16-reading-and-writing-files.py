# Exercise 16: Reading and Writing Files

# Import
from sys import argv

script, filename = argv
# Print
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# Check you want to continue 
raw_input("?")
# Open the file in 'write' mode, create if haven't.
print "Opening the file..."
target = open(filename, 'w')
# Remove content of the file
print "Truncating the file.   Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# Writing in the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Drill 3
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# Save the file
print "And finally, we close it."
target.close()

# Study Drills
#	1. If you do not understand this, go back through and use
#	the comment trick to get it squared away in your mind.
#	One simple English comment above each line will help
#	you understand or at least let you know what you need
#	to reearch more.
#	2. Write a script similar to the last exercise that uses
#	read and argv to read the file you just created.
#	3. There's too much repetition in this file. Use strings,
#	formats, and escapes to print out line1, line2, and
#	line3 with just one target.write() commant instead of six.
#	4. Find out why we had to pass a 'w' as an extra parameter
#	to open. Hint: open tries to be safe by making you explicitly
#	say you want to write a file.
#	5. If you open the file with 'w' mode, then do you really
#	need the target.truncate()? Read the documentation for
#	Python's open function and see if that's true.

# Drill 2
# Open saved file
open_file = open(filename, 'r')
# Read and print it
the_file = open_file.read()
print "This is the content of the file %s." % the_file

# Close, save it
open_file.close()

# Drill 5
# We don't need to use target.truncate() !!!

















