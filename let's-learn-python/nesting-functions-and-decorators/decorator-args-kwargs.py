def add_one(myFunc):
    def add_one_inside(*args, **kwargs):
        return myFunc(*args, **kwargs) + 1
    return add_one_inside

@add_one
def old_func(x = 3245):
    return x


print old_func()
