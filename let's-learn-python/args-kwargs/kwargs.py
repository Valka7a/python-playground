def Func(x = 234, y = 9):
    print x, y

Func(x = 100, y = 10)

def Func(**kwargs):
    for item in kwargs.items():
        print item

Func(me = "wat", you = 2)
