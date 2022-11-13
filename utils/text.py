from colorama import Fore, Back
import time


# Раскрашивает *args в цвет который указан в color
# Весь список цветом можно найти в colorama классе Fore
# Example: string_to_colored(Fore.RED, "Hello World", 1, 3)
# Result: возвращает string "Hello World 1 3" покрашенный в красный цвет
def colored(color: Fore = Fore.WHITE,
            *args) -> str:
    info: str = ""
    for i in args:
        info += str(i)

    return color + info + '\033[0m'


# Отпечатывает текс в машинописном стиле
# Example: text=Hello, delay=0.25
# Result: H [0.25sec] e [0.25sec] l [0.25sec] l [0.25sec] o [0.25sec]
# буква за буквой появляются через каждые 0.25 сек согласно примеру выше
def printing(text: str,
             delay: float = 0.1,
             _input: bool = False) -> str:
    for i in text:
        print(i, end="")
        time.sleep(delay)
    return _input if "" else text


# Отпечатывает вариант ошибки (всё красным текстом)
# Дёргает состояние "исключения" чтобы отпечатать проблему.
def error(text, e: Exception):
    print(colored(Fore.RED, text, ": ", str(e)))


class StringBuilder:
    text: str = None

    def __init__(self, text: str = ""):
        self.text = text

    def __str__(self) -> str:
        return self.text

    def __init(self):
        self.text = ""

    def append(self, var, end=" "):
        self.text += str(var) + end
        return self

    def append_red(self, var, end=" "):
        self.text += colored(Fore.RED, var) + end
        return self

    def append_green(self, var, end=" "):
        self.text += colored(Fore.GREEN, var) + end
        return self

    def append_blue(self, var, end=" "):
        self.text += colored(Fore.BLUE, var) + end
        return self

    def append_yellow(self, var, end=" "):
        self.text += colored(Fore.YELLOW, var) + end
        return self

    def append_white(self, var, end=" "):
        self.text += colored(Fore.WHITE, var) + end
        return self

    def append_black(self, var, end=" "):
        self.text += colored(Fore.BLACK, var) + end
        return self

    def append_cyan(self, var, end=" "):
        self.text += colored(Fore.CYAN, var) + end
        return self

    def append_ln(self):
        self.text += "\n"
        return self

    def append_tab(self):
        self.text += "\t"
        return self

    def containsIgnoreCase(self, text: str) -> bool:
        pass
