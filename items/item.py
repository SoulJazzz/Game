import enum

from utils.text import *
from utils.rnd import *
from enum import *


@unique
class ItemType(Enum):
    POTION = 0
    WEAPON = 1
    ARMOR = 2
    BOOK = 3
    QUEST = 4
    OTHER = 5


class Item:
    id: int = None
    name: str = None
    descr: str = None
    weight: float = None
    base_price: int = 0
    price_modifier: float = 0
    type: ItemType = ItemType.OTHER

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def is_wearable(self) -> bool:
        return self.type is ItemType.ARMOR \
               or self.type is ItemType.WEAPON

    def is_destroyable(self):
        return self.type is not ItemType.QUEST

    def is_sellable(self):
        return self.type is not ItemType.QUEST

    def set_rnd_base_price(self) -> int:
        self.base_price = round(rnd_get_minmax(10, 100) * self.price_modifier) if (self.type is not ItemType.QUEST) else 0
        return self.base_price

    def __str__(self) -> str:
        return StringBuilder() \
            .append_cyan(self.name).append("[", "").append_yellow(self.id, "").append("]", "").append_ln() \
            .append_yellow("Тип:").append_red(self.type.name).append_ln() \
            .append_yellow("Описание:").append_green(self.descr).append_ln() \
            .append_yellow("Вес:").append_red(self.weight).append_ln() \
            .append_yellow("Цена:").append_red(self.base_price, "Z").append_ln() \
            .append_yellow("Можно уничтожить:").append_red(self.is_destroyable()).append_ln() \
            .append_yellow("Можно продать:").append_red(self.is_sellable()).append_ln() \
            .append_yellow("Экипируемая:").append_red(self.is_wearable()).append_ln() \
            .text


weapon = Item(1, "Меч Дракулы", ItemType.WEAPON)
weapon.descr = "Клинок которым режут яйца - всем вампирам и нечисти."
weapon.weight = 1.76
weapon.price_modifier = 1.45
weapon.set_rnd_base_price()
print(weapon)

quest = Item(2, "Зуб дракона", ItemType.QUEST)
quest.descr = "Необходимый квестовый предмет для Larry NPC."
quest.weight = 0.05
print(quest)


potion = Item(2, "Малое зелье лечения", ItemType.POTION)
potion.descr = "Можно выпить и исцелить себе 50ОЗ... наверное..."
potion.weight = 0.15
potion.price_modifier = 0.25
potion.set_rnd_base_price()
print(potion)
