"""
EN
Write a program that connects the math module and, using the value of the number π from this module, finds the perimeter
of this circle for the radius of a circle passed to it on standard input and prints it to standard output.

RU
Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля, находит для
переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.

Sample Input:

10.0

Sample Output:

62.83185307179586
"""

import math

radius = float(input())

print(math.pi * (radius * 2))