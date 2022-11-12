from utils.text import *

# Максимальное кол-во мест в инвентаре
MAX_SPACE = 20


class Inventory:
    space: int = 0  # текущая забитость инвентаря
    items: dict = None  # предметы в инвентаре
    right_hand = None  # экипировано в правую руку
    left_hand = None  # экипировано в левую руку
    helmet = None  # экипированный шлем
    body = None  # экипированное тело
    gaiters = None  # экипированные штаны
    gloves = None  # экипированные перчатки
    boots = None  # экипированные ботинки

    def get_item_by_name(self, name):
        for i in self.items:
            item = self.items[i]
            if item.name is name:
                return item

    def get_item_by_index(self, index):
        return self.items[index]

    def del_item_by_name(self, name):
        index = -1
        for i in self.items:
            item = self.items[i]
            if item.name is name:
                index = i
                break

        if index != -1:
            item = self.items[index]
            print("Предмет " + str_to(Fore.RED, item.name) + " был удалён из инвентаря.")
            self.items[index] = None

    def del_item_by_index(self, index):
        item = self.items[index]
        print("Предмет " + str_to(Fore.RED, item.name) + " был удалён из инвентаря.")
        self.items[index] = None

    def enough_space(self) -> bool:
        return self.space < MAX_SPACE

    def add_item(self, item, index):
        self.items[index] = item

    def find_space(self) -> int:
        for i in self.items:
            item = self.items[i]
            if item is None:
                return i
