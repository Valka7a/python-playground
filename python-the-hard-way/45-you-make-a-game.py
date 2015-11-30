# Exercise 45: You Make a Game
"""
You need to start learning to feed yourself. Hopefully as you have worked through this 
book, you have learned that all the information you need is on the internet. You just
have to go search for it. The only thing you have been missing are the right words and 
what to look for when you search. Now you should have a sense of it, so it's about time 
you struggled through a big project and tried to get it working.

Here are your requirements:
	1. Make a different game from the one I made.
	2. Use more than one file and use import to use them. Make sure you know what that is.
	3. Use one class per room and give the classes names that fit their purpose (like 
	GoldRoom, KoiPondRoom).
	4. Your runner will need to know about these rooms, so make a class that runs them.
	There's plenty of ways to do this, but consider having each room return what room is
	next or setting a variable of what room is next.


Other than that I leave it to you. Spend a whole week on this and make it the best game
you can. Use classes, functions, dicts, lists, anything you can to make it nice. The
purpose of this lesson is to teach you how to structure classes that need other classes 
inside other files.

Remember, I'm not telling you exactly how to do this, because you have to do this yourself.
Go figure it out. Programming is problem solving and that means trying things, experimenting,
failing, scrapping your work and trying again. When you get stuck, ask for help and show
people your code. If they are mean to you, ignore them, focus on the people who are not
mean and offer to help. Keep working it and cleaning it until it's good, then show it some more.

Good luck and see you in a week with your game.
"""

# Evaluating Your Game
"""
In this exercise you will evaluate the game you just made. Maybe you got partway through it
and you got stuck. Maybe you got it working but just barely. Either way, we're going to go
through a bunch of things you should know now and make sure you covered them in your game.
We're going to study how to properly format a class, common converntions in using classes
and a lot of "textbook" knowledge.

Why would I have you try to do it yourself and then show you how to di it right? From now
on in the book I'm going to try to make you self-sufficient. I've been holding your hand
mostly this whole time and I can't do that for much longer. I'm now instead going to give
you things to do, have you do them on your own and then give you ways to improve what you
did.

You will Struggle at first and probably be verry frustrated but stick with it and eventually
you will build a mind for solving problems. You will start to find creative solutions to
problems rather than just copy solutions out of textbooks.
"""

# Function Style
"""
All the other rules I've taught you about to make a function nice apply here, but
add these things:
	* For various reasons, programmers call functions that are part of class "methods".
	It's mostly marketing but just be warned that every time you say "function" they'll
	annoyingly correct you and say "method". If they get too annoying, just ask them to
	demonstrate the mathematical basis that determines how a "method" is different from
	a "function" and they'll shut up.
	* When you work with classes much of your time is spent talking about making the 
	class "do things". Instead of naming your functions after what the function does, 
	instead name it as if it's a command you are giving to the class. Same as pop is 
	saying "Hey list, pop this off". It isn't called remove_from_end_of_list because 
	even though that's what it does, that's not a command to a list.
	* Keep your functions small and simple. For some reason when people start learning 
	about classes they forget this.
"""


# Class Style
"""
	* Your class should use "camel case" like SuperGoldFactory rather than
	super_gold_factory.
	* Try not to do too much in your __init__ functions. It makes them harder to use.
	* Your other functions should use "underscore format" so write my_awesome_hair and
	not myawesomehair or MyAwesomeHair.
	* Be consistent in how you organize your function arguments. If your class has to 
	deal with users, dogs and cats, keep that order throughout unless it really doesn't
	make sense. If you have one function that takes (dog, cat, user) and the other takes
	(user, cat, dog), it'll be hard to use.
	* Try not to use variables that come from the module or globals. They should be fairly
	self-contained.
	* A foolish consistency is the hobgoblin of little minds. Consistency is good, but
	foolishly following some idiotic mantra because everyone else does is bad style. Think
	for yourself.
	* Always, always have class Name(object) format or else you will be in big trouble.
"""


# Code Style
"""
	* Give your code vertical space so people can read it. You will find some very bad
	programmers who are able to write reasonable code but who do not add any spaces. This 
	is bad style in any language because the human eye and brain use space and vertical
	alignment to scan and separate visual elements. Not haveing spaces is the same as 
	giving your code an awesome camouflage paint job.
	* If you can't read it out loud, it's probably hard to read. If you are having a 
	problem making something easy to use, try reading it out loud. Not only does this 
	force you to slow down and really read it, but it also helps you find difficult 
	passages and things to change for readability.
	* Try to do what other people are doing in Python until you find your own style.
	* Once you find your own style, do not be a jerk about it. Working with other people
	code is part of being a programmer and other people have really bad taste. Trust me, 
	you will probably have really bad taste too and not even realize it.
	* If you find someone who writes code in a style you like, try writing something 
	that mimics that style.
"""

# Good Comments
"""
 * Programmers will tell you that your code should be readable enough that you do not
 need comments. They'll then tell you in their most official sounding voice, "Ergo one
 should never write comments or documentation. QED". Those programmers are either 
 consultants who get paid more if other people can't use their code, or incompetents who
 tend to never work with other people. Ignore them and write comments.
 * When you write comments, describe why you are doing what you are doing. They code 
 already says how, but why you did things the way you did is more important.
 * When you write doc comments for your functions, make the comments documentation for 
 someone who will have to use your code. You do not have to go crazy, but a nice little 
 sentence about what someone can do with that function helps a lot.
 * While comments are good, too many are bad and you have to maintain them. Keep your 
 comments relatively short, and to the point and if you change a function, review the 
 comment to make sure it's sitll correct.
 """

 # Evaluate Your Game
 """
 I want you to now pretend you are me. Adopt a very stern look, print out your code and
 take a red pen and mark every mistake you find, including anything from this exercise 
 and from other guidelines you've read so far. Once yu are done marking your code up, I
 want you to fix everything you came up with. Then repeat this a couple of times, looking 
 for anything that could be better. Use all the tricks I've given you to break your code 
 down into the smallest tiniest little analysis you can.

 The purpose of this exercise is to train your attention to detail on classes. Once you 
 are done with this bit of code, find someone else's code and do the same thing. Go through 
 a print copy of some part of it and point out all the mistakes and style errors you find.
 Then fix it and see if your fixes can be done without breaking that program.

 I want you to do nothing but evaluate and fix code for the week. Your own code and other 
 people's. It'll be pretty hard work, but when you are done your brain will be wired tight 
 like a boxer's hands.
 """






































