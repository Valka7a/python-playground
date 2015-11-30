# Exercise 0: The Setup
"""
This exercise has no code. It is simply the exercise you complete to get your
computer to run Python. You should follow these instructions as exactly as possible.
For example, Mac OS X computers already have Python 2, so do not install Python 3
(or any Python).

                       ______________________________________
                       |            WARNING                 |
                       |====================================|
                       | If you do not know how to use      |
                       | PowerShell on Windows, Terminal    |
                       | on OS X or bash on Linux then      |
                       | you need to go learn that first.   |
                       | You should do the exercises in     |
                       | Appendix A first before continuing |
                       | with these exercises.              |
                       --------------------------------------

"""


# Mac OS X
"""
Do the following tasks to complete this exercise:

1. Go to http://www.barebones.com/products/textwrangler/ with your browser, get
the TextWrangler text editor, and install it.
2. Put TextWrangler (your editor) in your dock so you can reach it easily.
3. Find your Terminal program. Search for it. You will find it.
4. Put your Terminal in your dock as well.
5. Run your Terminal program. It won't look like much.
6. In your Terminal program, run python. You run things in Terminal by just
typing the name and hitting RETURN.
7. Type quit(), Enter, and get out of python.
8. You should be back at a prompt similar to what you had before you typed python.
If not, find out why.
9. Learn how to make a directory in the Terminal.
10. Learn how to change into a directory in the Terminal.
11. Use your editor to create a file in this directory. You will make the file,
"Save" or "Save As...," and pick this directory.
12. Go back to Terminal using just the keyboard to switch windows.
13. Back in Terminal, list the directory with ls to see your newly created file.
"""

# OS X: What You Should See
"""
Here's me doing this on my OS X computer in Terminal. Your computer might be
different, but should be similar to this.
________________________________________________________________________________
Last login: Sat Apr 24 00:56:54 on ttys001
~ $ python
Python 2.5.1 (r251:54863, Feb  6 2009, 19:02:12)
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
~ $ mkdir mystuff
~ $ cd mystuff
mystuff $ ls
# ... Use TextWrangler here to edit test.txt....
mystuff $ ls
test.txt
mystuff $
________________________________________________________________________________
"""

# Windows
"""
1. Go to http://notepad-plus-plus.org/ with your browser, get the Notepad++ text
editor, and install it. You do not need to be the administrator to do this.
2. Make sure you can get to Notepad++ easily by putting it on your desktop and/or
in Quick Launch. Both options are available during setup.
3. Run PowerShell from the Start menu. Search for it and you can just press Enter
to run it.
4. Make a shortcut to it on your desktop and/or Quick Launch for your convenience.
5. Run your PowerShell program (which I will call Terminal later). It won't look
like much.
6. In your PowerShell (Terminal) program, run python. You run things in Terminal
by just typing the name and pressing Enter:

    1. If you run python and it's not there (python is not recognized..). Install
    it from http://python.org/download.

    2. Make sure you install Python 2, not Python 3.

    3. You may be better off with ActiveState Python especially when you do not
    have Administrative rights

    4. If after you install it python still isn't recognized then in PowerShell
    enter this:

        [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User")

    5. Close PowerShell and then start it again to make sure Python now runs. If
    it doesn't, restart may be required.

7. Type quit() and press Enter to exit python.
8. You should be back at a prompt similar to what you had before you typed python.
If not, find out why.
9. Learn how to make a directory in the PowerShell (Terminal).
10. Learn how to change into a directory in the PowerShell (Terminal).
11. Use your editor to create a file in this directory. Make the file, Save or
Save As... and pick this directory.
12. Go back to PowerShell (Terminal) using just the keyboard to switch windows.
up if you can't figure it out.
13. Back in PowerShell (Terminal), list the directory to see your newly created file.
********************************************************************************
From now on, when I say "Terminal" or "shell" I mean 'PowerShell' and that's what
you should use.

            _____________________________________________________________
            |                   WARNING                                 |
            |===========================================================|
            | Sometimes you install Python on Windows and it doesn't    |
            | configure the path correctly. Make sure you enter         |
            | [Environment]::SetEnvironmentVariable("Path",             |
            | "$env:Path;C:\Python27", "User") in PowerShell to         |
            | configure it correctly. You also have to either           |
            | restart PowerShell or your whole computer to get it to    |
            | really be fixed.                                          |
            -------------------------------------------------------------
"""

# Windows: What You Should See
"""
________________________________________________________________________________
> python
ActivePython 2.6.5.12 (ActiveState Software Inc.) based on
Python 2.6.5 (r265:79063, Mar 20 2010, 14:22:52) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
> mkdir mystuff
> cd mystuff
... Here you would use Notepad++ to make test.txt in mystuff ...
>
> dir
 Volume in drive C is
 Volume Serial Number is 085C-7E02

 Directory of C:\Documents and Settings\you\mystuff

04.05.2010  23:32    <DIR>          .
04.05.2010  23:32    <DIR>          ..
04.05.2010  23:32                 6 test.txt
               1 File(s)              6 bytes
               2 Dir(s)  14 804 623 360 bytes free

>
________________________________________________________________________________

It is still correct if you see different information than mine, but your should be
similar.
"""

# Linux
"""
Linux is a varied operating system with a bunch of different ways to install
software. I'm assuming if you are running Linux then you know how to install
packages so here are your instructions:

1. Use your Linux package manager and install the gedit text editor.
2. Make sure you can get to gedit easily by putting it in your window manager's
menu:
    1. Run gedit so we can fix some stupid defaults it has.
    2. Open Preferences and select the Editor tab.
    3. Change Tab width: to 4.
    4. Select (make sure a check mark is in) Insert spaces instead of tabs.
    5. Turn on "Automatic indentation" as well.
    6.Open the View tab and turn on "Display line numbers."
3. Find your Terminal program. It could be called GNOME Terminal, Konsole, or xterm.
4. Put your Terminal in your dock as well.
5. Run your Terminal program. It won't look like much.
6. In your Terminal program, run python. You run things in Terminal by just typing
the command name and pressing Enter:
    1. If you run python and it's not there, install it. Make sure you install
    Python 2 not Python 3.
7. Type quit() and press Enter to exit python.
8. You should be back at a prompt similar to what you had before you typed python.
If not, find out why.
9. Learn how to make a directory in Terminal.
10. Learn how to change into a directory in Terminal.
11. Use your editor to create a file in this directory. Typically you will make
the file, Save or Save As..., and pick this directory.
12. Go back to Terminal using just the keyboard to switch windows. Look it up if
you can't figure it out.
13. Back in Terminal, list the directory to see your newly created file.
"""

# Linux: What You Should See
"""
________________________________________________________________________________

$ python
Python 2.6.5 (r265:79063, Apr  1 2010, 05:28:39)
[GCC 4.4.3 20100316 (prerelease)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
$ mkdir mystuff
$ cd mystuff
# ... Use gedit here to edit test.txt ...
$ ls
test.txt
$
________________________________________________________________________________

It is still correct if you see different information than mine, but yours should
be similar.
"""

# Finding Thing on the Internet
"""
A major part of this book is learning to research programming topics online. I'll
tell you to "search for this on the internet," and your job is to use a search
engine to find the answer. The reason I have you search instead of just giving
you the answer is because I want you to be an independent learner who does not
need my book when you're done with it. If you can find the answers to your questions
online then you are one step closer to not needing me, and that is my goal.

Thanks to search engines such as Google you can easily find anything I tell you
to find. If I say, "search online for the python list functions" then you simply
do this:
    1. Go to http://google.com/
    2. Type: python list functions
    3. Read the websites listed to find the best answer.

"""

# Warnings for Beginners
"""
You are done with this exercise. This exercise might be hard for you depending on
your familiarity with your computer. If it is difficult, take the time to read and
study and get through it, because until you can do these very basic things you will
find it difficult to get much programming done.

If someone tells you to stop at a specific exercise in this book or to skip certain
ones, you should ignore that person. Anyone trying to hide knowledge from you, or
worse, make you get it from them instead of through your own efforts, is trying to
make you depend on them for your skills. Don't listen to them and do the exercises
anyway so that you learn how to educate yourself.

If a programmer tells you to use vim or emacs, just say "no." These editors are for
when you are a better programmer. All you need right now is an editor that lets you
put text into a file. We will use gedit, TextWrangler, or Notepad++ (from now on
called "the text editor" or "a text editor") because it is simple and the same on
all computers. Professional programmers use these text editors so it is good enough
for you starting out.

A programmer may try to get you to install Python 3 and learn that. Say, "When all
of the Python code on your computer is Python 3, then I'll try to learn it." That
should keep them busy for about 10 years. I repeat, do not use Python 3. Python 3
is not used very much, and if you learn Python 2 you can easily learn Python 3 when
you need it. If you learn Python 3 then you'll still have to learn Python 2 to get
anything done. Just learn Python 2 and ignore people saying Python 3 is the future.

A programmer will eventually tell you to use Mac OS X or Linux. If the programmer
likes fonts and typography, they'll tell you to get a Mac OS X computer. If he likes
control and has a huge beard, he'll tell you to install Linux. Again, use whatever
computer you have right now that works. All you need is an editor, a Terminal, and
Python.

Finally, the purpose of this setup helps you do three things very reliably while
you work on the exercises:
    1. Write exercises using your text editor, gedit on Linux, TextWrangler on
    OS X, or Notepad++ on Windows.
    2. Run the exercises you wrote.
    3. Fix them when they are broken.
    4. Repeat.

Anything else will only confuse you, so stick to the plan.
"""
