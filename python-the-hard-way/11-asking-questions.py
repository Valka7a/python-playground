# Exercise 11: Asking Questions

# Input and Print
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

# Print in sentence
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Study Drills
#	1. Go online and find out what Python's raw_input does.
#	2. Can you find other ways to use it? Try some of the samples you find.
#	3. Write another "form" like this to ask some other questions.
#	4. Related to escape sequences, try to find out why to last
#	line has '6\'2"' with that \' sequence. See how the single-quote needs
#	to be escaped because otherwise it would end the string?

# Drill 2, 3, 4
print "What mark car you like?",
mark = raw_input()
print "What model is it",
model = raw_input()
print "How much is it?",
price = raw_input()

print "So, the mark you like is %r and the model is %r at good price of %r." % (mark, model, price)
print 'So i need to have this %r in line.' % (height)