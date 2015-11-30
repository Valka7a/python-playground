# Exercise 15: Reading Files

# Import
from sys import argv

script, filename = argv

# Open a file
txt = open(filename)

# Print text
print "Here's your file %r:" % filename
# Print opened file and giving commant to read it
print txt.read()

# Drill 7
txt.close()
# Print text
print "Type the filename again:"

# Drill 4
# Write the file
#file_again = raw_input("> ")

file_again = filename
# End Drill 4
# Open the written file
txt_again = open(file_again)

# Print the file
print txt_again.read()
# Drill 7
txt_again.close()

# Study Drills
#	1. Above each line, write out in English what that line does.
#	2. If you are not sure ask someone for help or search online.
#	Many times searching for "python Thing" will find answers
#	to what that THING does in Python. Try searching for
#	"python open."
#	3. I used the word "commands" here, but commands are also called 
#	"functions" and "methods". You will learn about functions and 
#	methods later in the book.
#	4. Get rid of the lines 10-15 where you use raw_input and run
#	the script again.
#	5. Use only raw_input and try the script that way. Why is one
#	way of getting the filename would be better than another?
#	6. Start python to start the Python shell, and use open from
#	the prompt just like in this program. Notice how you can
#	open files and run read on them from within python?
#	7. Have your script also call close() on the txt and
#	txt_again variables. It's important to close files when you
#	are done with them.


# Drill 5
the_file = raw_input("Which file you want to open? ")
opened = open(the_file)
post = opened.read()

print "You want to open the file %r and the content is '%s'" % (the_file, post)

opened.close()