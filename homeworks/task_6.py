"""
EN
At that distant time, when Pasha went to school, he did not like Heron's formula for calculating the area of a triangle,
because it seemed too complicated. At one moment, Pavel decided to save all schoolchildren from suffering and
write and distribute to schools a program that calculates the area of a triangle on three sides.
One problem: since Paul did not like this formula, he did not remember it. Help him complete a good deed and write a
program that calculates the area of ​​a triangle given the lengths of its three sides using Heron's formula.
The input to the program is integers, the output of the program should be a number corresponding to the area triangle.

Sample Input:
3
4
5
Sample Output:
6.0

RU
В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади треугольника,
так как казалась слишком сложной. В один прекрасный момент Павел решил избавить всех школьников от страданий и
написать и распространить по школам программу, вычисляющую площадь треугольника по трём сторонам.
Одна проблема: так как эта формула не нравилась Павлу, он её не запомнил. Помогите ему завершить доброе дело и напишите
программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона.
На вход программе подаются целые числа, выводом программы должно являться вещественное число, соответствующее площади
треугольника.
"""

a, b, c = int(input()), int(input()), int(input())

p = (a + b + c) / 2

s = p * (p - a) * (p - b) * (p - c)
s = s ** 0.5
print(s)