def Func(*args):
    for arg in args:
        print arg


Func("me", "yoi", 1, 2, 5, 10)


l = [1, 2, 3, 4, "wat"]
# get every element
Func(*l)
