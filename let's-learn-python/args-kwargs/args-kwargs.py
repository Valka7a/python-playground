def Func(*args, **kwargs):
    for arg in args:
        print arg

    for item in kwargs.items():
        print item

# First args then kwargs
Func(12, 13, s = "wat", l = "taw")
