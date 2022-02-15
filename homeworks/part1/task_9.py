"""
EN
Residents of the country of Malevia often experiment with the layout of rooms. Rooms are triangular, rectangular and
round. To quickly calculate the living space, you need to write a program that receives the type of room figure and the
corresponding parameters as input, which would display the area of the resulting room.
For the number π in the country of Malevia, the value 3.14 is used.

The input format that the Malewians use is:

triangle
a
b
c
where a, b and c are the lengths of the sides of the triangle

rectangle
a
b
where a and b are the lengths of the sides of the rectangle

a circle
r
where r is the radius of the circle

Sample Input 1:

прямоугольник
4
10
Sample Output 1:
40.0

Sample Input 2:
круг
5

Sample Output 2:
78.5

RU
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и
соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.
Формат ввода, который используют Малевийцы:
треугольник
a
b
c
где a, b и c — длины сторон треугольника

прямоугольник
a
b
где a и b — длины сторон прямоугольника

круг
r
где r — радиус окружности
"""

pi = 3.14

user_choice = (input())

triangle = "треугольник"
rectangle = "прямоугольник"
circle = "круг"

if user_choice == triangle:
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif user_choice == rectangle:
    a, b = float(input()), float(input())
    s = a * b
    print(s)
elif user_choice == circle:
    r = float(input(""))
    s = pi * (r ** 2)
    print(s)