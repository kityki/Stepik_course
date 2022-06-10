"""
EN
A group of biologists at the Institute of Bioinformatics got themselves a turtle.

After training, the turtle learned to understand and remember the instructions of biologists of the following type:
north 10
west 20
south 30
east 40
where the first word is the direction the turtle should move, and the number after the word is the positive distance
in centimeters that the turtle should travel.

But the commands are given quickly, and the turtle crawls slowly, and the programmers figured out that you can write a
program that will determine where the biologists will eventually lead the turtle. To do this, programmers ask you to
write a program that will display the point at which the turtle will end up after all the commands. For simplicity, they
 decided to assume that the movement begins at the point (0, 0), and moving east increases the first coordinate, and
 north increases the second.

The program is given as input the number of commands nn that the turtle needs to execute, after which nn lines with the
 commands themselves. You need to output two numbers in one line: the first and second coordinates of the end point of
 the turtle. All coordinates are integer.

sample input:

four
north 10
west 20
south 30
east 40
sample output:

20 -20

RU
Группа биологов в институте биоинформатики завела себе черепашку.

После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное
расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу, которая
определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, которая
выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение начинается
в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.

Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего nn строк с самими командами.
Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты
целочисленные.

Sample Input:

4
север 10
запад 20
юг 30
восток 40
Sample Output:

20 -20
"""
lst = [0, 0]
n = int(input())
j = 0
direction_dict = {'north': 0, 'south': 0, 'west': 0, 'east': 0}
while j <= (n - 1):
    direction_input = input().split(' ')
    direction_input[1] = int(direction_input[1])
    j += 1
    if direction_input[0] == 'north':
        direction_dict['north'] = direction_input[1]
    elif direction_input[0] == 'south':
        direction_dict['south'] = direction_input[1]
    elif direction_input[0] == 'west':
        direction_dict['west'] = direction_input[1]
    elif direction_input[0] == 'east':
        direction_dict['east'] = direction_input[1]

print(direction_dict['north'] - direction_dict['south'], direction_dict['east'] - direction_dict['west'])