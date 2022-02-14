"""
EN
At the Institute of Bioinformatics, a robot moves around the office. Recently, students from a group of programmers
wrote for him a program according to which the robot, when it enters a room, counts the number of programmers in it
and says it aloud: "n programmers".
For this to sound correct, the correct word ending must be used for each n.
Write a program that reads an integer n (non-negative) from user input, outputting this number to
console, along with the word "programmer" correctly modified, so that the robot can communicate normally with
people, for example: 1 programmer, 2 programmers, 5 programmers.
There can be a lot of programmers in a room. Check that your program handles all cases correctly, like
up to at least 1000 people.

Sample Input 1:
5

Sample Output 1:
5 программистов

Sample Input 3:
1

Sample Output 3:
1 программист

RU
В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него
программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух:
"n программистов".
Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в
консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с
людьми, например: 1 программист, 2 программиста, 5 программистов.
В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как
минимум до 1000 человек.
"""
# 1
a = int(input())

if a == 1:
    print(f"{a} программист")
elif a % 10 == 1 or a % 100 == 1:
    print(f"{a} программист")
elif a == 12 or a == 13 or a == 14 or a == 11:
    print(f"{a} программистов")
elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
    print(f"{a} программиста")
elif a % 100 == 2 or a % 100 == 3 or a % 100 == 4:
    print(f"{a} программиста")
elif a == 0:
    print(f"{a} программистов")
else:
    print(f"{a} программистов")

# 2
i = int(input())
d = i % 10
h = i % 100
if d == 1 and h != 11:
    s = ""
elif 1 < d < 5 and not 11 < h < 15:
    s = "а"
else:
    s = "ов"
print(i, "программист" + s)