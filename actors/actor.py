from utils.text import *


class Actor:
    name = None
    hp = None
    strength = None
    intelligence = None
    agility = None
    isDead = False

    def reduceHp(self, attacker, damage):
        self.hp -= damage
        print("Получено: " + str_to(Fore.RED, str(damage)) + " ед. урона.")

    def isDead(self) -> bool:
        return self.isDead

    def getAttack(self) -> int:
        return self.strength
