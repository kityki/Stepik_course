"""
English
Kate knows that she needs to sleep X minutes. Unlike Nick, she goes to sleep after midnight at H hours and M minutes.
Help Kate to determine the time she should set on an alarm.

Sample Input 1:
480
1
2

Sample Output 1:
9
2

RU
Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится спать после полуночи в H часов и M минут.
Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через XX минут после того,
как она ляжет спать.

На стандартный ввод, каждое в своей строке, подаются значения X, H и M. Гарантируется, что Катя должна проснуться в
тот же день, что и заснуть. Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы,
во второй — минуты.
"""

minutes, at_hours, at_min = int(input()), int(input()), int(input())

hour_1 = at_hours * 60 + minutes + at_min
hour = hour_1 // 60
mino = hour * 60
left_min = hour_1 - mino
print(hour)
print(left_min)

