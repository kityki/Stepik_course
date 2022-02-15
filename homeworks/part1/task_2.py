"""
English
Nick goes to sleep at midnight, and he's figured out his optimal sleep time is X minutes. Nick wants to set the alarm
to ring in X minutes after midnight. It's necessary to set ring time in format hh: mm. Help Nick to
decide at what time to set the alarm?
Sample Input 2:
512
Sample Output 2:
8
32
____________________
RU
Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет X минут.
Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через X минут после полуночи, однако для этого
необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить, на какое время завести будильник.
Часы и минуты в выводе программы должны располагаться на разных строках (см. пример работы программы)
Помните, что для считывания данных нужно вызывать функцию input без аргументов!
"""

# 1
minutes = int(input())

hour = minutes // 60
hour_1 = hour * 60
left_min = minutes - hour_1
print(hour)
print(left_min)

# 2

#minutes = int(input())
#print(minutes // 60)
#print(minutes % 60)
