# RECRUSION - FUNKCIQ DA IZVIKA SEBE SI !!!

n = 0
i = int(raw_input("What will be the increment? : "))
m = int(raw_input("What will be the max number? : "))
def how(n):
	print "The number is: ", n
	if n == m:
		print "That was it!"
		return 1
	else:
		n = how(n + i)
		return n

how(n)