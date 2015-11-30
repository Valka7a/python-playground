"""
1. Create a function that prints out individual elements of lists within lists ..
2. Repeat problem #1 using recursion
3. Repeat problem #1 using "type(yourList) == list" to chech to see that the passed
argument is a list type
4. Repeat problem #1-3 for a keyword argument
5. You are awesome!
"""

# 1.
def list_within_list(outerlist, *args, **kwargs):
    for innerlist in outerlist:
        for item in innerlist:
            print (item)


# 2 & 3
def recursive_list(outerlist, *args, **kwargs):
    if outerlist and type(outerlist) == list:
        for innerlist in outerlist:
            if type(innerlist) == list:
                recursive_list(innerlist)
            else:
                print (innerlist)




# 4.
def best_recursive_list(*args, **kwargs):
    for outerlist in list(args) + list(kwargs.values()):
        if type(outerlist) == list:
            for innerlist in outerlist:
                if type(innerlist) == list:
                    best_recursive_list(innerlist)
                else:
                    print (innerlist)



if __name__ == '__main__':
    L1 = [[1, 2], [3,4]]
    L2 = [[[1], 3], [4, 5]]
    L3 = [[[32, [234, '', 'HAM', [42342],
            [345], 3456, 4576], 456, 100], 555]]

#    list_within_list(L1, L1, L1)
#    recursive_list(L2)
    best_recursive_list(L1, L2, mylist = L3)

    print ("You're a sexy beast!")
