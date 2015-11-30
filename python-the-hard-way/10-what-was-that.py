# Exercise 10: What Was That?

# "I am 6'2\" tall." # escape double-quote inside string
# 'I am 6\'2" tall.' # escape single-quote inside string

# Variables
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Print
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Escape Sequences
#	\\	=	Backslash (\)
#	\'	=	Single-quote (') 
#	\"	=	Double-quote (")
#	\a 	=	ASCII bell (BEL)
#	\b 	= 	ASCII backspace (BS)
#	\f 	= 	ASCII formfeed (FF)
#	\n 	= 	ASCII linefeed (LF)
#	\N{name}  	=	Character named name in the Unicode database (Unicode only)
#	\r ASCII  	=	Carriage Return (CR)
#	\t ASCII	=	Horizontal tab 	(TAB)
#	\uxxxx 	= 	Character with 16-bit hex value xxxx (Unicode only)
#	\Uxxxxxxxx 	= 	Character with 32-bit hex value xxxxxxxx (Unicode only)
#	\v 	=	ASCII vertical tab 	(VT)
#	\ooo = 	Character with octal value ooo
#	\xhh =	Character with hex value hh




# !!!!!!!!!!!!!  	Study Drills	!!!!!!!!!!!!!!!!!!
#	1. Memorize all the escape sequences by putting them on flash cards.
#	2. Use ''' (triple-single-quote) instead. Can you see why you might 
#	use that instead of """?
#	3. Combine escape sequences and format strings to create a more complex format.
#	4. Remember the %r format? Combine %r with double-quote and single-quote escapes
# 	and print them out. Compare %r with %s. Notice how %r prints it the way you'd write
# 	it in your file, but %s prints it the way you'd like to see it?

# Drill 2
slim_cat = '''
I can use the triple single quote,
because i don't have single quote
in my lines.
'''

print slim_cat

# Drill 3
complex_from = """
While my new game start\nI will play\tGod of War and will eat:\nMeat with\t POTATOES!
"""

print complex_from

# Drill 4
will = "ll"
combine_formats = "I\'%s use my %r from mine %r \"%r\" robots." % (will, 4, 6, "Powerful")

print combine_formats












