"""
English
Write a program:
Daniel slips X hours at night and Y minutes at daytime. How many minutes does he sleep during the day?

RU
Напишите программу:
Тимофей обычно спит ночью X часов и устраивает себе днем тихий час на Y минут. Определите, сколько всего минут
Тимофей спит в сутки.
Внимание, программа принимает значения X и Y из стандартного потока ввода (функция input), результат надо выводить
в стандартный поток вывода (функция print). Обратите внимание на то, что приглашение, переданное в качестве аргумента
в функцию input, считается выводом вашей программы.
"""

x, y = int(input()), int(input())
print(x * 60 + y)