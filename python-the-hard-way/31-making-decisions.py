# Exercise 31: Making Decisions

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Turn back quietly"
	print "4. Look around"

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off.		Good job!"
	elif bear == "2":
		print "The bear eats your legs off. 	Good job!"
	elif bear == "3":
		print "One plank creaked and bear eats you. 	Good job!"
	elif bear == "4":
		print "There have rifle. Will you get it?"
		print "1. Yes!"
		print "2. No!"

		rifle = raw_input("> ")

		if rifle == "1":
			print "Did you want to shoot the bear?"
			print "1. Yes, of course!"
			print "2. No!"

			choice = raw_input("> ")

			if choice == "1":
				print """
				The rifle isn't loaded! 
				You look around and see bullets on the table.
				You are going to get them,
				but the bear see you and eat you!!!
				Good job! :D
				"""

			elif choice == "2":
				print "While you thinking what to do the bear see you and eat you! 	Good job!"
			
			else:
				print "You can't choice other, for that you die! Good Job!"

		elif rifle == "2":
			print """
			This is stupid decision
			and what will do now?
			Okey, just die. Good job!
			"""
		else:
			print "You can't choce other, for that you die! Good Job!"

	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. 	Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. 	Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"


# Study Drills:
#	1. Make new parts of the game and change what decisions people
#	can make. Expand the game out as much as you can before it get
#	ridiculous.
#	2. Write a copletely new game. Maybe you don't like this one, so
#	make your own. This is your computer, do what you want.