"""
EN
Write a program that reads a string with the number n, which specifies the number of numbers to be counted.
Then reads n lines with numbers Xi, one number per line. There will be n+1 lines in total.
When reading the number x_ix i the program should output the value f(Xi).
The function f(x) is already implemented and available for calling.

The function is calculated long enough and depends only on the passed xx argument.
In order to meet the time limit, you need to avoid recalculating values.

RU
Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
Далее считывает nn строк с числами Xi, по одному числу в каждой строке. Итого будет n+1 строк.
При считывании числа Xi программа должна на отдельной строке вывести значение f(Xi). Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента xx. Для того, чтобы уложиться в
ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:

5
5
12
9
20
12
Sample Output:

11
41
47
61
41
"""

d = {}
for _ in range(int(input())):
    x = int(input())
    if x not in d:
        d[x] = f(x)
    print(d[x])
