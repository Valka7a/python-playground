# Exercise 28: Boolean Practice

True and True 														#	True
False and True 														#	False
1 == 1 and 2 == 1 													#	False
"test" == "test"													#	True
1 == 1 or 2 != 1 													#	True
True and 1 == 1 													#	True
False and 0 != 0 													#	False
True or 1 == 1														#	True
"test" == "testing" 												#	False
1 != 0 and 2 == 1 													#	False
"test" != "testing"													#	True
"test" == 1															#	False
not (True and False) 												#	True
not (1 == 1 and 0 != 1)												#	False
not (10 == 1 or 1000 == 1000)										# 	False
not (1 != 10 or 3 == 4)												# 	False
not ("testing" == "testing" and "Zed" == "Cool Guy") 				#	True
1 == 1 and (not ("testing" == 1 or 1 == 0)) 						#	True
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) 					#	False
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) 		#	False

# 1. Find an equality test (== or !=) and replace it with its truth.
# 2. Find each 'and/or' inside parentheses and solve those first.
# 3. Find each 'not' and invert it
# 4. Find any remaining 'and/or' and solve it.
# 5. When you are done you should have True or False.

# Example with line 22:
3 != 4 and not ("testing" != "test" or "Python" == "Python")	# line 22: False

1 != 2 and 2 != 3												# line 05: True
False and 0 != 1 												# line 09: False
"test" != "testing" 											# line 11: True
1 == 1 or 2 != 3 												# line 12: True
"test" != 1														# line 14: True
not (False and True)											# line 15: True
not (1 != 0 and 0 == 0)											# line 16: False
not (10 != 1 or 1000 != 1001) 									# line 17: False
not ("me" == "me" or 3 != 4)									# line 18: False
not ("testing" != "test" and "Zed" != "Bad Guy") 				# line 19: False
1 != 2 and not ("you" != 5 or 12 != 21)							# line 20: False
"chunky" != "bacon" and not (7 != 2 or 1 != "Play")				# line 21: False



# Study Drills:
#	1. There are a lot of operators in Python similar to '!=' and
#	'=='. Try to find as many "Equality operators" as you can.
#	They should be like '<' or '<='
#	2. Write out the names of each of these equality operators.
#	For example, I call '!=' "not equal".
#	3. Play with the Python by typing out new boolean operators,
#	and before you press Enter try to shout out what it is. Do
#	not think about it. Shout the first thig that comes to mind.
#	Write it down, then press Enter, and keep track of how many
#	you get right and wrong.
#	4. Throw away the piece of paper from 3 away so you do not
#	accidentally try to use it later.


# Drill 1:
# ==	(Equal to)
# !=	(Not equal to)
# > 	(Greater than)
# >=	(Greater than or equal to)
# < 	(Less than)
# <=	(Less than or equal to)









