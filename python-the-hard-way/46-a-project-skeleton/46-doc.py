# Exercise 46: A Project Skeleton

"""
This will be where you start learning how to set up a good project "skeleton" directory.
This skeleton directory will have all the basics you need to get a new project up and 
running . It will have your project layout, automated tests, modules and install scripts.
When you go to make a new project, just copy this directory to a new name and edit the 
files to get started.
"""

# Installing Python Packages
"""
Before you can begin this exercise you need to install some software for Python by using
a tool called "pip" to install new modules. Here's the problem though. You are at a point 
where it's difficult for me to help you do that and keep this book sane and clean. There
are so many ways to install software on so many computers that I'd have to spend 10 pages 
walking you through every step and let me tell you I am a lazy guy.

Rather than tell you how to do it exactly, I'm going to tell you what you should install 
and then you tell you to watch the video that accompanies this exercise and follow along.
You will have to struggle with this part of the exercise though as giving accurate and 
current installation instructions is tricky. Computers change frequently so you may have 
to do some research if you get stuck.

Install the following Python packages:
	1. pip from: 			http://pypi.python.org/pypi/pip
	2. distribute from: 	http://pypi.python.org/pypi/distribute
	3. nose from: 			http://pypi.python.org/pypi/nose/
	4. virtualenv: from:	http://pypi.python.org/pypi/virtualenv


Do not just download these packages and install them by hand. Instead see how other people 
recommend you install these packages and use them from your particular system. The process 
will be different for most verions of Linux, OSX and definitely different for Windows. 

I am warning you; this will be frustrating. In the business we call this "yak shaving". Yak 
shaving is any activity that is mind numbingly, irritatingly boring and tedious that you 
have to do before you can do something else that's more fun. You want to create cool Python 
projects, but you can't do that until you set up a skeleton directory, but you can't set up 
a skeleton directory until you install some packages, but you can't install packages until 
you install package installers and you can't install package installers until you figure out 
how your system installs software in general and so on.

Struggle through this anyway. Consider it your trial by annoyance to get into the programmer 
club. Every programmer has to do these annoying tedious tasks before they can do something 
cool.

								NOTE
				Sometimes the Python installer does not add the 
				C:\Python27\Script to the system PATH. If this 
				is the case for you, go back and add this to the 
				path just like you did for C:\Python27 in Exercise 0 with:

				[Environment]::SetEnvironmentVariable("Path",
				"$env:Path;C:\Python27\Scripts", "User")
"""


# Creating the Skeleton Project Directory
"""
First, create the structure of your skeleton directory with these commands:
$ mkdir projects
$ cd projects/
$ mkdir skeleton
$ cd skeleton
$ mkdir bin NAME tests docs


I use a directory named projects to store all the various things I'm working on. inside 
that directory I have my skeleton directory that i put the basis of my projects into.
The directory NAME will be renamed to whatever you are calling your project's main module 
when you use the skeleon.

Next we need to set up some initial files. Here's how you do that on Linxu/OSX:
$ touch NAME/__init__.py 
$ touch tests/__init__.py 


Here's the same thing on Windows PowerShell:
$ new-item -type file NAME/__init__.py 
$ new-item -type file tests/__init__.py 


That creates an empty Python module directories we can put our code in. Then we need to 
create a setup.py file we can use to install our project later if we want:

try:
	from setuptools import setup
except ImportErrors:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)

Edin this file so that it has your contact information and is ready to go for 
when you copy it.


Finally you will want a simple skeleton file for tests named tests/NAME_tests.py:

from nose.tools import *
import NAME

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"
"""


# Final Directory Structure
"""
When you are done setting all of this up, your directory should look like mine here:

skeleton/
	NAME/
		__init__.py 
	bin/
	docs/
	setup.py
	tests/
		NAME_tests.py
		__init__.py


And from now on, you should run your commands from that work with this directory
from this point. If you can't do 'ls -R' and see this same structure, then you are 
in the wrong place. For example, people commonly go into the tests/ directory to 
try to run files there, which won't work. To run your application's test, you would 
need to be ABOVE tests/ and this location I have above. So, if you try this:

$ cd tests/ 	# WRONG! WRONG! WRONG!
$ nosetests

Remember this because people make this mistake quite frequently
"""


# Testing Your Setup
"""
After you get all that installed you should be able to do this:
$ nosetests
.
----------------------------------------------------------------------
Ran 1 test in 0.007s

OK


I'll explain what this nosetests thing is doing in the next exercise, but for now if
you do not see that, you probably got something wrong. Make sure you put __init__.py
files in your NAME and tests directories and make sure you got test/NAME_tests.py right.
"""

# Using the Skeleton
"""
You are now done with most of your yak shaving. Whenever you want to start a new project, 
just do this:
	1. Make a copy of your skeleton directory. Name it after your new project.
	2. Rename (move) the NAME directory to be the name of your project or whatever 
	you want to call your root module.
	3. Edit your setup.py to have all the information for your project.
	4. Rename tests/NAME_tests.py to also have your module name.
	5. Double check it's all working by using nosetests again.
	6. Start coding.
"""


# Required Quiz
"""
This exercise doesn't have Study Drills but a quiz you should complete:
	1. Read about how to use all of the things you installed.
	2. Read about the setup.py file and all it has to offer. Warning: it is not 
	a very well-written piece of software, so it will be verry strange to use.
	3. Make a project and start putting code into the modue, then get the module working.
	4. Put a script in the bin directory that you can run. Read about how you can make 
	a Python script that's runnable for your system.
	5. Mention the bin script you created in your setup.py so that it gets installed.
	6. Use your setup.py to install your own module and make sure it works, then use 
	pip to uninstall it.
"""























