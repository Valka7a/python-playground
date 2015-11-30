# Exercise 19: Functions and Varibles
# Define function with 2 values and print
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# Call the function with numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Call the function with variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call the function with math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Call the function with combine variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Study Drills
#	1. Go back through the script and type a comment above
#	each line explaining in English what it does.
#	2. Start at the bottom and read each line backward, saying
#	all the important characters.
#	3. Write at least one more function of your own design, and
#	run it 10 different ways.

# Drill 3
def car_and_price(cars, prices):
	print "%s is good mark cars." % cars
	print "The price %d $ is good for %s." % (prices, cars)

# First call
print "First way to call the function:"
car_and_price("Mercedes", 5000)

# Second call
print "Second way to call the funtion:"
mark = "Mercedes"
money = 5000

car_and_price(mark, money)

# Third call
print "Third way to call the function:"
car_and_price("Mercedes", 4000 + 1000)

# Fourth call
print "Fourth way to call the function:"
money = 400 + 600 + 4000

car_and_price("Mercedes", money)

# Fifth call
print "Fifth way to call the function:"
mark = "Mer" + "cedes"
money = 5000

car_and_price(mark, money)

# Sixth call
print "Sixth way to call the function:\n", car_and_price("Mercedes", 5000)

# Seventh call
print "Seventh way to call the function:"
mark = "Me" + "rce" + "des"
money = 500 + 500 + 1000 + 3000

car_and_price(mark, money)

# Eighth call
print "Eighth way to call the function:"

car_and_price("Mer" + "ced" + "es", 4000 + 1000)

# Ninth call
print "Ninth way to call the function:"
mark = str(raw_input("What mark cars you like? "))
money = float(raw_input("How much is it? "))

car_and_price(mark, money)

# Tenth call
print "Tenth way to call the function:"
model = "Merce"
mark = model + "des"

car_and_price(mark, 5000)


































