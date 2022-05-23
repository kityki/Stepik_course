"""
EN
Write a program that takes a list of numbers as input in one line. The program must for each element of this list
print the sum of its two neighbors. For list elements that are extreme, one of the neighbors is the element located at
the opposite end of this list. For example, if the input is the list "1 3 5 6 10", then the output is expected to
be the list "13 6 9 15 7" (without quotes).

If only one number came to the input, you need to output it.

The output should contain a single line with the numbers of the new list separated by a space.

RU
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся
крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход
подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

Sample Input 1:

1 3 5 6 10
Sample Output 1:

13 6 9 15 7
Sample Input 2:

10
Sample Output 2:

10
"""
t = tuple(map(int, input().split()))
if len(t) != 1:
    t = tuple(t[i[0]-2] + t[i[0]] for i in enumerate(t))
print(*(t[1:] + t[:1]))