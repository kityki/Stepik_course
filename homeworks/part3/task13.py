"""
EN
Write a program that takes on standard input a list of soccer team games with match results and prints a summary table of the results of all matches on standard output.

A team is awarded 3 points for a win, 0 for a loss, and 1 for a draw.

The input format is as follows:
The first line contains an integer nn — the number of completed games.
This is followed by nn lines, which contain the results of the game in the following format:
First_team;Scored by_first_team;Second_team;Scored by_second_team

The program output should look like this:
Team:Total_games Wins Draws Losses Total_points

A specific I/O example is shown below.

The order in which commands are output is arbitrary.

sample input:

3
Spartak;9;Zenith;10
Locomotive;12;Zenith;3
Spartak;8;Locomotive;15
sample output:

Spartak:2 0 0 2 0
Zenith:2 1 0 1 3
Locomotive:2 2 0 0 6

RU
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
"""

