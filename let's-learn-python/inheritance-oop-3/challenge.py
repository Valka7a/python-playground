from abc import ABCMeta, abstractmethod


class Human(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self):
        pass

    def run(self):
        print ('running!')


class Robot(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self):
        pass

    def vacuum(self):
        print ('vacuuming!')


class Cyborg(Human, Robot):
    def __init__(self):
        super(Cyborg, self).__init__()


if __name__ == '__main__':
    try:
        h = Human()
    except:
        print ('Could not create a Human.')
    try:
        r = Robot()
    except:
        print ('Could not create a Robot')

    c = Cyborg()
    c.run()
    c.vacuum()
