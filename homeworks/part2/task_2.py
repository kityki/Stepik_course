"""
EN
At the Institute of Bioinformatics, a competition is organized between computer scientists and biologists.
The winners of the competition will get a big and tasty pie. The team of biologists has aa people, and the team of
computer scientists has bb people.

It is necessary to cut the pie in advance in such a way that it is possible to distribute pieces of the pie to any team
that won the competition, while each member of this team must get the same number of pieces of the pie. And since you
don't want to cut the pie into too small pieces, you need to find the minimum suitable number.

Write a program to find this number.
The program should read the sizes of the commands (two positive integers aa and bb, each number is entered on a
separate line) and output the smallest number dd that is divisible by both of these numbers without a remainder.

RU
В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования
достанется большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — bb человек.

Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей
соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не
хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

Напишите программу, которая помогает найти это число.
Программа должна считывать размеры команд (два положительных целых числа aa и bb, каждое число вводится на отдельной
строке) и выводить наименьшее число dd, которое делится на оба этих числа без остатка.
"""

a, b = int(input()), int(input())
c = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(int(c / (a + b)))