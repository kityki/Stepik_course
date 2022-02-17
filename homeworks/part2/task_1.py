"""
EN
Write a program that calculates the standard input of a numbers, and after the
first input of zero, it gives the sum of the all numbers before zero.
Sample Input 1:
5
-3
8
4
0

Sample Output 1:
14

Sample Input 2:
0

Sample Output 2:
0

RU
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого
введенного нуля выводит сумму полученных на вход чисел.
"""
# 1
sum_of_numbers = 0
i = 5
a = 1
while a != 0:
    a = int(input())
    sum_of_numbers += a
    if a == 0:
        print(sum_of_numbers)

# 2
a = int(input())
s = 0
while a != 0 :
    s += a
    a = int(input())
print(s)
