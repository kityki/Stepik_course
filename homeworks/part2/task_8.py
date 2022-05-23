"""
EN
Write a program that takes a single string of integers as input. The program should print the sum of these numbers.

Use the string split method.

RU
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки.

Sample Input:

4 -1 9 3
Sample Output:

15

"""
my_list = input().split()
my_list = list(my_list)

int_my_list = list(map(int, my_list))
sum_of_digits = 0
for i in int_my_list:
    sum_of_digits += i
print(sum_of_digits)

