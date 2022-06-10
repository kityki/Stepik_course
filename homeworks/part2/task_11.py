"""
EN
Write a program that reads numbers from the console (one per line) until the sum of the entered numbers is 0 and
immediately after that prints the sum of the squares of all the numbers read.

It is guaranteed that at some point the sum of the entered numbers will be equal to 0, after which there is no need
to continue reading.

In the example, we read the numbers 1, -3, 5, -6, -10, 13; at this point, we notice that the sum of these numbers is
equal to zero and print the sum of their squares, ignoring the fact that there are still unread values.

RU

Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не
будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,после этого считывание продолжать не нужно.

В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим
сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.

Sample Input:

1
-3
5
-6
-10
13
4
-8

Sample Output:

340
"""

a1 = int (input())
s = a1
s2 = 0+abs(a1**2)
while s != 0:
    a1 = int(input())
    s = s + a1
    s2 = s2+abs(a1)**2
    if s==0:
        break
print(s2)

