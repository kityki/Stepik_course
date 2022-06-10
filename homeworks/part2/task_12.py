"""
EN
Write a program that prints part of the sequence 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (a number is repeated as many times
as it is equal to). A non-negative integer n is passed to the input of the program — this is how many elements of the
sequence the program should display. The output is expected to be a sequence of numbers separated by a space in one
line.

For example, if n = 7, then the program should output 1 2 2 3 3 3 4.

RU
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется
столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов
последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через
пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

Sample Input:

7
Sample Output:

1 2 2 3 3 3 4

"""

n = int(input())
some_list = []
for i in range(1, n + 1):
    for j in range(i):
        some_list.append(i)
        if len(some_list) == n:
            print(*some_list)