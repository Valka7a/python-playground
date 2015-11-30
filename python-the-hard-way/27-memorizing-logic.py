# Exercise 27: Memorizing Logic

#The Truth Terms:
#	and
#	or
#	not
#	!= (not equal)
#	== (equal)
#	>= (greater-than-equal)
#	<= (less-than-equal)
#	True
#	False

# The Truth Tables

# NOT Table
#____________________________
#|		NOT		|	TRUE?	|
#----------------------------
#|	not False	|  True 	|
#|	not True 	|  False 	|
#----------------------------


# OR Table									 AND Table
#____________________________				________________________________
#|		OR 		 | 	TRUE?	|				| 		AND 		| 	TRUE? 	|
#----------------------------				---------------------------------
#| True or False  |  True 	|				| True and False	| 	False	|
#| True or True   |  True 	|				| True and True 	|	True 	|
#| False or True  |  True 	|				| False and True 	| 	False	|
#| False or False |  False	|				| False and False 	| 	False	|
#----------------------------				---------------------------------


# NOT OR Table 								  NOT AND Table	
#____________________________________		_________________________________
#| 		  NOT OR 		| 	TRUE? 	|		| 		NOT AND 		| TRUE? |
#------------------------------------		---------------------------------
#| not (True or False)  | 	False 	|		| not (True and False)	| True 	|
#| not (True or True) 	| 	False 	|		| not (True and True) 	| False |
#| not (False or True) 	| 	False	|		| not (False and True) 	| True  |
#| not (False or False) | 	True 	|		| not (False and False) | True  |
#------------------------------------		---------------------------------


# !=(Not Equal) Table 				 ==(Equal) Table
#____________________ 				_____________________
#| 	  !=	| TRUE? |				|	==		| TRUE? |
#--------------------				---------------------
#| 1 != 0 	| True  |				| 1 == 0	| False |
#| 1 != 1 	| False |				| 1 == 1	| True  |
#| 0 != 1 	| True  |				| 0 == 1  	| False |
#| 0 != 0 	| False |				| 0 == 0  	| True 	|
#-------------------- 				---------------------