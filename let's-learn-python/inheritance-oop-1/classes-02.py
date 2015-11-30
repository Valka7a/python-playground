class Character(object):

    def __init__(self):
        self.health = 100
        self.name = 20


class Blacksmith(Character):

    def __init__(self):
        super(Blacksmith, self).__init__()


bs = Blacksmith()
