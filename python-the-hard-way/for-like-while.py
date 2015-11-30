u = 0
n = int(raw_input("What will be max number? : "))
step = int(raw_input("What increment you want? : "))
lists = []

def while_for(u):
	for u in range(0, n, step):
		print "At the beginning i is %d" % u
		lists.append(u)

while_for(u)

print "The numbers are: "
for num in lists:
	print num