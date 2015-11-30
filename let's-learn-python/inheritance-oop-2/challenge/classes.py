import base as Base

class ChangeX(Base.BaseClass):
    def __init__(self):
        self.x = 17

class ChangeHam(Base.BaseClass):
    def __init__(self):
        super(BetterHam, self).__init__()

    def printHam(self):
        print ('Ham2')

class Combo(ChangeX, ChangeHam):
    def __init__(self):
        super(Combo, self).__init__()


if __name__ == '__main__':
    c = Combo()
    c.printHam()
    print (c.x)
    print (Base.BaseClass.__subclasses__())
