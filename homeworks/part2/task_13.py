"""
EN
Write a program that reads a list of numbers lstlst from the first line and a number xx from the second line, which
outputs all the positions where the number xx occurs in the given list lstlst.

Positions are numbered from zero, if the number xx is not found in the list, output the string "Missing" (without
quotes, with a capital letter).

Positions should be displayed in one line, in ascending absolute value.

RU
Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит
все позиции, на которых встречается число xx в переданном списке lstlst.

Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с
большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:

5 8 2 7 8 8 2 4
8
Sample Output 1:

1 4 5
Sample Input 2:

5 8 2 7 8 8 2 4
10
Sample Output 2:

Отсутствует

"""

lst = [int(i) for i in input().split()]
n = int(input())

for i in range(len(lst)):
    if lst[i] == n:
        print(i, end=" ")
if n not in lst:
    print("Отсутствует")