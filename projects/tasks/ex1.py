''' Challenge
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

items = [x for x in input('Enter words separated with comma: ').split(',')]
items.sort()
print(','.join(items))
