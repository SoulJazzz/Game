from utils.text import *
from containers.inventory import *


class Actor:
    name = None
    hp = None
    strength = None
    intelligence = None
    agility = None
    isDead = False
    isPlayer = False
    inv: Inventory = Inventory()

    def reduceHp(self, attacker, damage):
        self.hp -= damage
        if self.isPlayer:
            print("Получено урон: " + str_to(Fore.RED, damage) + " ед. урона от " + attacker.name)

    def isDead(self) -> bool:
        return self.isDead

    def getAttack(self) -> int:
        return self.strength