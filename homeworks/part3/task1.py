"""
EN
Write a function f(x) that returns the value of the following function defined on the entire number line:
Only the function needs to be implemented, the solution must not implement I/O operations.

RU
Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

Sample Input 1:

4.5
Sample Output 1:

7.25
Sample Input 2:

-4.5
Sample Output 2:

-5.25
Sample Input 3:

1
Sample Output 3:

-0.5
"""

def f(x):
    if x <= -2:
        result = 1 - ((x + 2)**2)
        return result
    elif -2 < x <= 2:
        result = - (x / 2)
        return result
    elif 2 < x:
        result = ((x - 2)**2) + 1
        return result