"""
1. Create a inheritance tree with the following structure
    1. BaseCharacter
        1. Non-Playable Character(NPC)
            1. Friendly
            2. Enemy
        2. Playable Character(PC)
            1. Archer
            2. Green Lantern
            3. Butcher
2. Add 'printName' function All characters have
3. Add 'self.attackDamage = 5' attr for all enemies
4. Create weapon class within same file
5. Have all PC characters start with a weapon
"""

class BaseCharacter(object):

    def printName(self):
        print (self.name)

class NonPlayableCharacter(BaseCharacter):
    pass

class NPCFriendly(NonPlayableCharacter):
    pass

class NPCEnemy(NonPlayableCharacter):

    def __init__(self):
        self.attackDamage = 5


class Weapon(object):
    pass


class PlayableCharacter(BaseCharacter):

    def __init__(self):
        self.weapon = Weapon()


class PCArcher(PlayableCharacter):
    pass

class PCGreenLantern(PlayableCharacter):
    pass

class PCButcher(PlayableCharacter):
    pass


if __name__ == '__main__':
    enemy = NPCEnemy()
    print (enemy.attackDamage)
    butcher = PCButcher()
    print (butcher.weapon)
