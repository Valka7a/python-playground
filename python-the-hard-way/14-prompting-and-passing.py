# Exercise 14: Prompting and Passing

# Import
from sys import argv

script, user_name = argv
prompt = '>> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


# Study Drills
#	1. Find out what Zork and Adventure were. Try to find a copy and play it.
#	2. Change the prompt variable to something else entirely.
#	3. Add another argument and use it in your script, the same
#	way you did in the previous exercise with first, second = ARGV.
#	4. Make sure you understand how i combined a """ style multiline sting
#	with the % format activator as the last print.


# Drill 2

prompt = '< '

print "Hello %s, this is %s script." % (user_name, script)
print "Do you want more %s?" % user_name
wants = raw_input(prompt)

print "Why you don't want more %s?" % user_name
answer = raw_input(prompt)

print """
Okey, so your name is %s.
And you tells %s more.
Because, %s.
""" % (user_name, wants, answer)

# Drill 3
# script, user_name, nick_name ... = argv