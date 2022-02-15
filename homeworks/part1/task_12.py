"""
EN
Pasha loves to ride public transport, and when he receives a ticket, he immediately checks whether he is lucky.
A ticket is considered lucky if the sum of the first three digits matches the sum of the last three digits of the
ticket number. However, Pasha is very bad at calculating in his mind, so he asked you to write a program that will
check the equality of the sums and print "Lucky" if the sums are the same, and "Regular" if the sums are different.
The input to the program is a string of six digits.
You only need to display the word "Happy" or "Regular", with a capital letter.

Sample Input 1:
090234

Sample Output 1:
Счастливый

Sample Input 2:
123456

Sample Output 2:
Обычный

RU
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и
выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

"""

# 1
my_str = str(input(""))

a = int(my_str[0])
b = int(my_str[1])
c = int(my_str[2])
d = int(my_str[3])
e = int(my_str[4])
f = int(my_str[5])
num_1 = a + b + c
num_2 = d + e + f

if num_1 == num_2:
    print("Счастливый")
else:
    print("Обычный")


# 2

a, b, c, d, e, f = input()
n = int(a) + int(b) + int(c)
m = int(d) + int(e) + int(f)
if n == m:
    print('Счастливый')
else:
    print('Обычный')

