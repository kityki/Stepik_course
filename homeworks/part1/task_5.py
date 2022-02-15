"""
EN
It is required to determine whether the given year is a leap year.
Recall those leap years are those years whose serial number is either a multiple of 4, but not a multiple of 100,
or a multiple of 400 (for example, 2000 was a leap year, and 2100 will be a non-leap year).
The program should work correctly on numbers 1900≤n≤3000.
Print "Leap year" if the given year is a leap year and "Normal" otherwise
(do not forget to check the case of the characters output by the program).
Sample Input 1:

2100
Sample Output 1:

Обычный
Sample Input 2:

2000
Sample Output 2:

Високосный

RU
Требуется определить, является ли данный год високосным.
Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4, но при этом не кратен 100,
либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
Программа должна корректно работать на числах 1900≤n≤3000.
Выведите "Високосный" в случае, если считанный год является високосным и "Обычный" в обратном случае (не забывайте
проверять регистр выводимых программой символов).
"""

enter_year_number = int(input())

if enter_year_number % 400 == 0 or enter_year_number % 4 == 0 and enter_year_number % 100 != 0:
    print("Високосный")
else:
    print("Обычный")