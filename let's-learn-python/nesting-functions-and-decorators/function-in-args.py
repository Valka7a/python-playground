def add_one(myfunc):
    def add_one_inside():
        return myfunc() + 1
    return add_one_inside

def old_func():
    return 3

newFunc = add_one(old_func)
print old_func(), newFunc() # old_func return 3 , newFunc return 4
