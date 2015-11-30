# Exercise 33: While Loops

# While-loop runs until the expressions is False.
# to avoid never stop the loop have some rules:
#	1. Make sure that you use 'while-loop' sparingly.
#	Usually a 'for-loop' is better.
#	2. Review your while statements and make sure that
#	the boolean test will become 'False' at some point.
#	3. When in doubt, print out your test variable at the
#	top and bottom of the 'while-loop' to see what it's doing.

# make variable, and variable with list
i = 0
# Drill 2
n = int(raw_input("What will be the max number? : "))
numbers = []

# while variable is less than 6 do.. and save it in list
# Drill 1
def call_while(i):
	# change i < 6 to i < variable
	# Drill 3
	r = int(raw_input("How much you want to be the increment? : "))
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)

		# variable is euqal to variable + 1
		# Drill 3
		i += r
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

call_while(i)
print "The numbers: "

# for every in variable print...
for num in numbers:
	print num



# Study Drills:
#	1. Convert this 'while-loop' to a function that you can call and 
#	replace '6' in the test(i < 6) with a variable.
#	2. Use this function to rewrite the script to try different numbers.
#	3. Add another variable to the function arguments that you can pass
#	in that lets you change the '+ 1' on line 8 so you can change how
#	much it increments by.
#	4. Rewrite the script again to use this function to see what effect
#	that has.
#	5. Write it to use 'for-loop' and 'range'. Do you need the incrementor
#	in the middle anymore? What happens if you do not get rid of it?

# Drill 5 No i don't need to use += 1
# Drill All drills:
u = 0
n = int(raw_input("What will be max number? : "))
step = int(raw_input("What increment you want? : "))
lists = []

def while_for(u):
	for u in range(0, n, step):
		print "At the beginning i is %d" % u
		lists.append(u)

		print "Numbers now: ", lists

while_for(u)

print "The numbers are: "
for num in lists:
	print num











