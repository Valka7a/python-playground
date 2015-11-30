# Exercise 5: More Variables and Printing

name = 'Valentin K. Dur.'
age = 24 # not a lie
height = 170 # sm
weight = 57 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d kilo tall." % height
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)