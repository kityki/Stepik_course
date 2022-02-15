"""
English
Anya learned from the Health program that it is recommended to sleep at least A hours a day, but oversleeping is also
harmful, it's better to sleep less than B hours. Anya now sleeps HH hours a day. If there is a sleep mode, a transfer
recommendation is required "Health", output "It's OK". If Anya sleeps less than AA hours, enter “Lack of sleep”,
if more than BB hours, then output "Sprinkle".
The resulting number A is always or less than B.
The three-line entry program supplies variables in the following order: A, B, H.

Sample Input 1:

6
10
8
Sample Output 1:

Это нормально
Sample Input 2:

7
9
10
Sample Output 2:

Пересып
Sample Input 3:

7
9
2
Sample Output 3:

Недосып
_________
RU
Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не
стоит спать более B часов. Сейчас Аня спит HH часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи
“Здоровье”, выведите “Это нормально”. Если Аня спит менее AA часов, выведите “Недосып”, если же более BB часов, то
выведите “Пересып”.

Получаемое число A всегда меньше либо равно B.

На вход программе в три строки подаются переменные в следующем порядке: A, B, H.
"""

a, b, h = int(input()), int(input()), int(input())

if h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
else:
    print("Это нормально")