#My first project on the python.

from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.BLACK)
print(Back.CYAN)
a = float(input('Введи число: '))
print(Back.MAGENTA)
znak = input('Выбери действие: ( +, -, *, / ) ')
print(Back.CYAN)
b = float(input('Введи второе число: '))
print(Back.YELLOW)
if znak == '+':
    c = a + b
    print(c)
elif znak == '*':
    c = a * b
    print(c)
elif znak == '-':
    c = a - b
    print(c)
elif znak == '/':
    c = a / b
    print(c)
else:
    print(Back.RED)
    print('Что-то пошло не так')

input()
