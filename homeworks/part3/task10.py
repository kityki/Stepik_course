"""
EN
Write a program that runs from the console and prints the values of all passed arguments to the screen (you don't need to display the script name). Do not change the order of the arguments in output.

To access the program's command-line arguments, include the sys module and use the argv variable from that module.

An example of the program's operation:

> python3 my_solution.py arg1 arg2
arg1 arg2

RU
Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран (имя скрипта
выводить не нужно). Не изменяйте порядок аргументов при выводе.

Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.

Пример работы программы:

> python3 my_solution.py arg1 arg2
arg1 arg2
"""

import sys
for i in sys.argv[1:]:
    print(i, end=" ")