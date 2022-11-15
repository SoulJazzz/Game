from utils.text import *


class Actor:
    name: str = None
    hp = None
    strength = None
    intelligence = None
    agility = None
    isDead = False

    def __init__(self, name):
        self.name = name

    def isDead(self) -> bool:
        return self.isDead

    def get_atk(self) -> int:
        pass

