class Actors:
    hp = None
    strength = None
    intelligence = None
    agility = None

    def __init__(self, hp=1000, strength=28, intelligence=18, agility=26):
        self.hp = hp
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

    def reduceHp(self) -> int:
        pass

    def sDead(self) -> bool:
        pass

    def getAttack(self):
        pass


Actors()
