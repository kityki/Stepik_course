"""
EN
Recently, we counted for each word the number of its occurrences in a string. But all words may not be as interesting
to look at as, for example, the most commonly used ones.

Write a program that reads text from a file (there may be more than one line in the file) and outputs the most frequent
word in this text and, separated by a space, how many times it occurred. If there are several such words, output the
first one lexicographically (you can use the < operator for strings).

Give the output of the program as your answer, not the program itself.

Words written in different registers are considered the same.

sample input:

abc a bCd bC AbC BC BCD bcd ABC

sample output:

abc 3

RU
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически
первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:

abc a bCd bC AbC BC BCD bcd ABC

Sample Output:

abc 3
"""

with open('task7_txt_file.txt') as inf:
    all_words = inf.read().lower().strip().split()
    all_words.sort()
    #print(all_words)
    c = 1

l = []
word_dict = dict()
for i in all_words:
    g = all_words.count(i)
    l.append(g)
    word_dict = dict(zip(all_words, l))
#print(word_dict)
maxi = 1
for i, j in word_dict.items():
    if j > maxi:
        maxi = j
        print(i, maxi)