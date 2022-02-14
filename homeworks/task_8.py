"""
EN
Write a simple calculator that reads three strings from user input: the first number, the second number and an
operation, then applies the operation to the entered numbers ("first number" "operation" "second number") and displays
the result on the screen.

Supported operations: +, -, /, *, mod, pow, div, where
mod is taking the remainder of the division,
pow - exponentiation,
div is an integer division.

If the division is being performed and the second number is 0, the string "Division by 0!" should be output.

Please note that real numbers come to the input of the program.

Sample Input 1:
5.0
0.0
mod

Sample Output 1:
Деление на 0!

Sample Input 2:
-12.0
-8.0
*

Sample Output 2:
96.0

RU
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и
операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
"""

a, b = float(input()), float(input())
c = input("")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif (c == "/" or c == "div" or c == "mod"):
     if b == 0:
         print("Деление на 0!")
     else:
         print(a / b)
elif c == "*":
    print(a * b)
elif c == "mod":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a % b)
elif c == "pow":
    print(a ** b)
elif c == "div":
    if b == 0:
        print("Деление на 0!")
    else:
        print(a // b)