def add_one(myFunc):
    def add_one_inside():
        return myFunc() + 1
    return add_one_inside

def old_func():
    return 3

oldfunc = add_one(old_func)
print oldfunc()
