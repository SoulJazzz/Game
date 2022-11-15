from actors.actor import Actor
from actors.instances.player import Player
from utils.generators.dragon_generator import Dragon, createDragon
from utils.text import StringBuilder, printing


class History:
    def tellStory(self, teller: Actor, player: Player):
        pass


class DragonHistory(History):
    dragon: Dragon

    def __init__(self):
        self.dragon = createDragon()

    def tellStory(self, teller: Actor, player: Player):
        dialog = StringBuilder()
        dialog.append("Я расскажу тебе историю о драконе по имени").append_cyan(self.dragon.имя)\
            .append("который хотел").append_cyan(self.dragon.цели).append_ln()\
            .append("Но недавно его потревожили и он").append_cyan(self.dragon.привязанность).append_ln()\
            .append("Он считает, что").append_cyan(self.dragon.слабость).append_ln()\
            .append("Его можно узнать по").append_cyan(self.dragon.облик).append("и").append_cyan(self.dragon.манеры).append_ln()
        printing(dialog)

