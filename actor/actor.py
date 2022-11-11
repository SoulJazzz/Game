class Actor:
    name = None
    hp = None
    strength = None
    intelligence = None
    agility = None

    isDead: bool = False

    def reduceHp(self) -> int:
        pass

    def isDead(self) -> bool:
        return self.isDead

    def getAttack(self) -> int:
        pass

    def die(self):
        self.isDead = True
        self.hp = 0
        print(self.name + " мёртв.")
