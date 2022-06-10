"""
EN
Write a program that takes a list of numbers on one line as input and prints the values on one line to the screen.
that occur more than once.

To solve the problem, the sort list method can be useful.

The output numbers should not be repeated, the order of their output can be arbitrary.

RU
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
Sample Input 1:

4 8 0 3 4 2 0 3
Sample Output 1:

0 3 4
Sample Input 2:

10
Sample Output 2:

Sample Input 3:

1 1 2 2 3 3
Sample Output 3:

1 2 3
Sample Input 4:

1 1 1 1 1 2 2 2
Sample Output 4:

1 2
"""

a = list(input().split())
a = list(map(int, a))
b = []
for index, letter in enumerate(a):
    if letter in a[index+1:]:
        b.append(letter)

b = set(b)
print(*b)


