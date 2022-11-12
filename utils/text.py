from colorama import Fore, Back
import time


# Раскрашивает *args в цвет который указан в color
# Весь список цветом можно найти в colorama классе Fore
# Example: string_to_colored(Fore.RED, "Hello World", 1, 3)
# Result: возвращает string "Hello World 1 3" покрашенный в красный цвет
def str_to(color: Fore, *args) -> str:
    info: str = ""
    for i in args:
        info += str(i)

    return color + info + '\033[0m'


# Отпечатывает текс в машинописном стиле
# Example: text=Hello, delay=0.25
# Result: H [0.25sec] e [0.25sec] l [0.25sec] l [0.25sec] o [0.25sec]
# буква за буквой появляются через каждые 0.25 сек согласно примеру выше
def print_as_machine(text: str, delay: int):
    for i in text:
        print(i, end="")
        time.sleep(delay)


# Отпечатывает вариант ошибки (всё красным текстом)
# Дёргает состояние "исключения" чтобы отпечатать проблему.
def error(text, e: Exception):
    print(str_to(Fore.RED, text + ": " + str(e)))
