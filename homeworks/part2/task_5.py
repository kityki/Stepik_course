"""
EN

Write a program that reads two numbers a and b from the keyboard, calculates and prints the average to the console
arithmetic of all numbers from the interval [a; b][a;b] that are multiples of 3.

In the example below, the arithmetic mean is calculated for numbers in the interval [-5; 12].
There are 66 numbers divisible by 33 in this segment: -3, 0, 3, 6, 9, 12.
Their arithmetic mean is 4.5

The input to the program is intervals within which there is always at least one number that is divisible by 3.

RU

Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее
арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 3.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12].
Всего чисел, делящихся на 33, на этом отрезке 66: -3, 0, 3, 6, 9, 12.
Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.

Sample Input:

-5
12
Sample Output:

4.5

"""

a, b = int(input()), int(input())
count = 0
sum = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        count += 1
arif = sum / count
print(arif)