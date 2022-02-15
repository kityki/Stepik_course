"""
EN
Write a program that takes three integers as input, one number per line, and outputs to the console in three lines,
first the maximum, then the minimum, then the remaining number.
Repeating numbers can also be submitted for input.
Sample Input 1:
8
2
14

Sample Output 1:
14
2
8

RU
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в
три строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.
"""
# 1
a, b, c = int(input()), int(input()), int(input())

if a >= b >= c:
    print(a, c, b, sep="\n")
elif a >= c >= b:
    print(a, b, c, sep="\n")
elif b >= a >= c:
    print(b, c, a, sep="\n")
elif b >= c >= a:
    print(b, a, c, sep="\n")
elif c >= a >= b:
    print(c, b, a, sep="\n")
elif c >= b >= a:
    print(c, a, b, sep="\n")

# 2

a, b, c = int(input()), int(input()), int(input())

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a)
print(b)
print(c)

