# Exercise 43: Basic Object-Oriented Analysis and Design

# Process to build something to evolve problems
#	1. Write or draw about the problem.
#	2. Extract key concepts from 1 and research them.
#	3. Create a class hierarchy and object map for the concepts.
#	4. Code the classes and a test to run them.
#	5. Repeat and refine.



# The Analysis of a Simple Game Engine

# Write or Draw About the Problem

"""
Aliens have invaded a space ship and our hero has to go through a maze of rooms 
defeating them so he can escape into an escape pod to the planet below. The game 
will be more like a Zork or Adventure type game with text outputs and funny ways 
to die. The game will involve an engine that runs a map full of rooms or scenes. 
Each room will print its own description when the player enters it and then tell 
the engine what room to run next out of the map.
"""

# At this point I have a good idea for the game and how it would run, so now I want
# to describe each scene:

"""
	Death
		This is when the player dies and should be something funny.
	Central Corridor
		This is the starting point and has a Gothon already standing there.
		They have to defeat with a joke before continuing.
	Laser Weapon Armory
		This is where the hero gets a neutron bomb to blow up the ship before
		getting to the escape pod. It has a keypad the hero has to gues the
		number for.
	The Bridge
		Another battle scene with a Gothon where the hero places the bomb.
	Escape Pod
		Where the hero escapes but only after guessing the right escape pod.
"""


# Extract Key Concepts and Research Them

# First I make a list of all the nouns:
# Alien, Player, Ship, Maze, Room, Scene, Gothon, Escape Pod, Planet, Map, Engine, Death,
# Central Corridor, Laser Weapon Armory, The Bridge


# Create a Class Hierarchy and Object Map for the Concepts
"""
Right away I see that "Room" and "Scene" are basically the same thing depending on how 
I want to do things. I'm going to pick "Scene" for this game. Then I see that all the 
specific rooms like "Central Corridor" are basically just Scenes. I see also that Death 
is basically a Scene, which confirms my choice of "Scene" over "Room" since you can have 
a death scene, but a death room is kind of odd. "Maze" and "Map" are basically the same 
so I'm going to go with "Map" since I used it more often. I don't want to do a battle 
system so I'm going to ignore "Alien" and "Player" and save that for later. The "Planet"
could also just be another scene instead of something specific
"""

# After all of that thoiught process I start to make a class hierarchy that looks
# like this in my text editor:
#	* Map
#	* Engine
#	* Scene
#		* Death
#		* Central Corridor
#		* Laser Weapon Armory
#		* The Bridge
#		* Escape Pod


"""
I would then go through and figure out what actions are needed on each thing based on 
verbs in the description. For example, I know from the description I'm going to need a 
way to "run" the engine, "get the next scene" from the map, get the "opening scene" and 
"enter" a scene. I'll add those like this:
"""
#	* Map
#		- next_scene
#		- opening_scene
#	* Engine
#		- play
#	* Scene
#		- enter
#		* Death
#		* Central Corridor
#		* Laser Weapon Armory
#		* The Bridge
#		* Escape Pod

"""
Notice how I just put -enter under Scene since I know that all the scenes under it will 
inherit it and have to override it later.
"""


# Code the Classes and a Test to Run Them
# The Code for "Gothons from Planet Percal #25"
from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        print "What will you do?"
        print ">> shoot!"
        print ">> dodge!"
        print ">>tell a joke"

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead.  Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know: "
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "This is the code: %s." % code
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
        print "What will you do?"
        print ">> throw the bomb"
        print ">>slowly place the bomb"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        print "Fast look tells you %s is good." % good_pod
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


# Top Down vs Bottom Up

# Steps to do Bottom Up:
#	1. Take a small piece of the problem; hack on some code and get it to run barely.
#	2. Refine the code into something more formal with classes and automated tests.
#	3. Extract the key concepts you're using and try to find research for them.
#	4. Write a description of what's really going on.
#	5. Go back and refine the code, possibly throwing it out and starting over.
#	6. Repeat, moving on to some other piece of the problem.



# Study Drills:
#	1. Change it! Maybe you hate this game. Could be to violent, you aren't into sci-fi. Get the game
#	working, then change it to what you like. This is your computer, you make it do what you want.
#	2. I have a bug in this code. Why is the door lock guessing 11 times?
# 	3. Explain how returning the next room works.
#	4. Add cheat codes to the game so you can get past the more difficult rooms. I can do this with 
#	two words on one line.
#	5. Go back to my description and analysis, then try to build a small combat system for the hero 
#	and the various Gothons he encounters.
#	6. This is actually a small version of something called a "finite state machine". Read about them.
#	They might not make sense but try anyway.




























