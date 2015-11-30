def add_one(myFunc):
    def add_one_inside():
        return myFunc() + 1
    return add_one_inside

@add_one
def old_func():
    return 3

print old_func()
