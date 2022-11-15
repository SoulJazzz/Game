class Weapon:
    """Оружие """
    name = None
    attack = None
    enchant = None
    price = None

    def __init__(self, name, attack, enchant, price):
        self.name = name
        self.attack = attack
        self.enchant = enchant
        self.price = price

    def equip(self):
        pass

    def unequip(self):
        pass


hermit_spear = Weapon(name='Копьё отшельника', attack=127, enchant=0, price=None)
blunted_sword_in_battles = Weapon(name='Затупившийся меч в боях', attack=87, enchant=0, price=None)
candy_corn_ax = Weapon(name='Топор из конфетной кукурузы', attack=105, enchant=0, price=None)

print(hermit_spear.name)
print(blunted_sword_in_battles.name)
print(candy_corn_ax.name)