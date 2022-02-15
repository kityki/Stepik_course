"""
EN
Write a program that takes an integer as input and outputs True if the input value falls within the interval (-15, 12]
\cup (14, 17) \cup [19, +\infty)(−15,12]∪(14 ,17)∪[19,+∞) and False otherwise (character case matters).

Notice the different parentheses used to indicate spacing. The task uses semi-open and open intervals. You can read
more about this, for example, on Wikipedia (half-interval, interval).

Sample Input 1:
20
Sample Output 1:
True

Sample Input 2:
-20
Sample Output 2:
False

RU
Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал
(-15, 12] \cup (14, 17) \cup [19, +\infty)(−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и
открытые интервалы. Подробнее про это вы можете прочитать, например, на википедии (полуинтервал, промежуток).
"""

a = int(input())
if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
    print(True)
else:
    print(False)