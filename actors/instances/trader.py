from utils.generators.dragon_history import *
from utils.text import printing, ARROW_RIGHT, dialogue
import os


class Trader(Actor):
    history: History = DragonHistory()
    listItems: list = None

    def sell(self, buyer: Player):
        # fixme: insert logic
        """Продаёт предмет"""
        choice = input()
        print(self.listItems[int(choice) - 1])

    def show_products(self):
        pass

    def talk(self):
        """Функция в которой игрок разговаривает с NPC Trader"""

        # Приветствие игрока
        dialogue(self.name,
                 StringBuilder()
                 .append("О! Не каждый день встретишь странника, который умеет оценить хороший товар.", "")
                 .append_ln()
                 .text)

        # Переменная про запрос имени
        whats_your_name = StringBuilder() \
            .append("Как тебя зовут?") \
            .append_yellow(ARROW_RIGHT) \
            .append_ln().text

        # Запрос: Ввод на запрос об имени от игрока
        opt1 = dialogue(self.name, whats_your_name, 0.02, True)

        # Ответ: Продолжение вопросов от торговца
        dialogue(self.name,
                 StringBuilder()
                 .append("Хм... ").append_ln()
                 .append_red(opt1, ", ")
                 .append("кха-кха-кха, ой, прости, кашель.")
                 .append("Раньше таких имён я не слышал.")
                 .append_ln()
                 .text)

        # Запрос: История о драконе
        want_listen_a_story = StringBuilder() \
            .append("Хочешь я расскажу тебе историю о Драконе?") \
            .append_yellow(ARROW_RIGHT, "").text

        # Ответ: Ввод на запрос об имени от игрока
        opt2 = dialogue(self.name, want_listen_a_story, 0.02, True)

        match opt2:
            case "Да" | "да" | "yes" | "y" | "yeah":
                self.history.tellStory(self, None)
            case "Нет" | "нет" | "no" | "n" | "nope":
                printing(StringBuilder()
                         .append("Теперь давай вернёмся к нашим делам.")
                         .append_ln("Смотри, оценивай и покупай!")
                         .text)

                # Показываем лист продуктов, которые можно купить
                self.show_products()
            case _:
                printing("Я без понятия чего ты хочешь, можешь повторить?")


trader = Trader("Джон Вик")
trader.talk()
