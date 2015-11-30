# Exercise 35: Branches and Functions

from sys import exit
# Creating function for gold room
def gold_room():
    print "This room is full of gold.  How much kilo do you take?"
# Make a choice
    choice = raw_input("> ")
# If-else statement
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

# Creating function for bear room
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
# Make variable for moving bear to False
    bear_moved = False
# Createing while True loop with choice and if,elif, else statement
    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
# Drill 4
        elif "shoot" in choice:
        	print "You kill the bear, and eat it. Good Job!"
        else:
            print "I got no idea what that means."

# Creating function for cthulhu room with choice if,elif, else statement
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# Create function for die with reason
def dead(why):
    print why, "Good job!"
    exit(0)
# Create function to start everything with choice, if,elif, else statement
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# Call Start function
start()



# Study Drill:
#	1. Draw a map of the game and how you flow through it.
#	2. Fix all of your mistakes, including spelling mistakes.
#	3. Write comments for the functions you don't understand.
#	4. Add more to the game. What can you do to both simplify
#	and expand it?
#	5. The 'gold_room' has a waird way of getting you to type 
#	a number. What are all the bugs in this way of doing it?
#	can you make it better than what i've written? Look at
#	how 'int()' works for clues.









































