from utils.text import *


class Trader:
    """Торговец"""

    name = 'Хамфри'
    listItems: list = ['▶ Копьё отшельника', '▶ Затупившийся меч в боях',
                       '▶ Топор из конфетной кукурузы']

    def showList(self):
        """Показывает список предметов"""
        print([x for x in self.listItems])

    def sell(self):
        """Продаёт придмет"""
        choice = input()
        print(self.listItems[int(choice) - 1])

    def talk(self):
        """Разговор с игроком"""
        print_as_machine("О! Не каждый день встретишь странника, который умеет оценить хороший товар.\n", 0.1)
        name = input(print_as_machine_input('Как тебя зовут?\n➤ ', 0.1))
        print_as_machine('Хм...' + str_to(Fore.LIGHTRED_EX, str(name))
                         + ' Кха-кха-кха, ой, прости, кашель,\n'
                         + 'Раньше таких имён я не слышал.\n', 0.1)
        print_as_machine(' Хочешь я расскажу тебе историю о Красном Драконе?\n➤ ', 0.1)
        story = input()
        if story == 'Да'.lower():
            print_as_machine('Вы внимательно слушаите историю о Красном Драконе...\n', 0.1)
            print_as_machine('Теперь давай вернёмся к нашим делам.\n Что ты хочешь купить? \n', 0.1)
            count = 0
            for l in self.listItems:
                count += 1
                print(str(count) + ' ' + str_to(Fore.GREEN, l))
            self.sell()
        else:
            print_as_machine('Тогда вернёмся к нашим делам, Что ты хочешь купить?\n', 0.1)
            count = 0
            for l in self.listItems:
                count += 1
                print(str(count) + ' ' + str_to(Fore.GREEN, l))
            self.sell()


trade = Trader()
print(trade.talk())
