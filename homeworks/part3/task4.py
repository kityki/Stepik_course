"""
EN
When Anton read "War and Peace", he became interested in how many words and in what quantity are used in this book.

Help Anton write a simplified version of such a program that can count space-separated words and display the resulting statistics.

The program should read one line from the standard input and output for each unique word in this line the number of its repetitions (case insensitive) in the format "word count" (see output example).
The order of output of words can be arbitrary, each unique word must be output only once.

RU
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное словo должно выводиться только один раз.

Sample Input 1:

a aa abC aa ac abc bcd a
Sample Output 1:

ac 1
a 2
abc 2
bcd 1
aa 2
Sample Input 2:

a A a
Sample Output 2:

a 3

"""
some_string = input().lower().split()
for i in sorted(set(some_string)):
    result = some_string.count(i)
    print(i, result)