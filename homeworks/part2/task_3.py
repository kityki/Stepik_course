"""
EN

For each number entered check:
if the number is less than 10, then skip this number;
if the number is greater than 100, then stop reading the numbers;
otherwise, print this number back to the console on a separate line.

RU
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

Sample Input 1:
12
4
2
58
112

Sample Output 1:
12
58
"""

while True:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    print(a)