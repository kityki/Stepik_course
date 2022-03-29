"""
EN

RU

Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень
пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].

Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и
строка таблицы.

Sample Input 1:

7
10
5
6
Sample Output 1:

	5	6
7	35	42
8	40	48
9	45	54
10	50	60
"""

a, b, c, d = int(input()), int(input()), int(input()), int(input())

for g in range(c, d + 1):
    print('\t', g, end = '')
for h in range(a, b + 1):
    print('\n', h, end = '')
    for j in range(c, d + 1):
        print('\t', h * j, end = '')
    print(end = '')
