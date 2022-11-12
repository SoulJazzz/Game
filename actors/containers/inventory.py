from utils.text import *

# Максимальное кол-во мест в инвентаре
MAX_SPACE = 20


class Inventory:
    space: int = 0  # текущая забитость инвентаря
    items: list = [None] * MAX_SPACE  # предметы в инвентаре
    right_hand = None  # экипировано в правую руку
    left_hand = None  # экипировано в левую руку
    helmet = None  # экипированный шлем
    body = None  # экипированное тело
    gaiters = None  # экипированные штаны
    gloves = None  # экипированные перчатки
    boots = None  # экипированные ботинки

    def get_item_by_name(self, name):
        for item in self.items:
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
        if item is None:
            return
        else:
            print("Предмет " + str_to(Fore.RED, item.name) + " был удалён из инвентаря.")
            self.items[index] = None

    def enough_space(self) -> bool:
        return self.space < MAX_SPACE

    def replace(self, item, index: int):
        self.items[index] = item

    def add_item(self, item):
        try:
            index: int = self.find_space()
            self.items[index] = item
        except Exception as e:
            error("Ошибка в containers/inventory.py/add_item(self, item)", e)

    def find_space(self) -> int:
        index = 0
        for item in self.items:
            if item is None:
                return index
            else:
                index += 1

        return -1

    def show(self):
        print([x for x in self.items])
