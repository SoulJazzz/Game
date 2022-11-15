from actors.actor import Actor
from actors.containers.inventory import Inventory
from items.item import Item
from utils.text import colored, Fore


class Player(Actor):
    inventory: Inventory = Inventory()
    target: Actor = None
    item: Item = None

    def is_have_target(self) -> bool:
        return self.target is not None

    def is_target_dead(self) -> bool:
        return self.target.isDead

    def equip(self):
        active_item: Item = self.inventory.get_item_by_name(self.item.name)
        if active_item is None or active_item.is_wearable() is False:
            print("Вы не можете одеть предмет " + colored(Fore.RED, active_item.name) + " потому, что этот предмет нельзя экипировать.")
        else:
            self.inventory.set_equipment(active_item)
            print("Вы экипировали предмет " + colored(Fore.RED, active_item.name) + " в " + colored(Fore.RED, active_item.slot))
