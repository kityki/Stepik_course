"""
EN
The simplest spell checker can be based on a list of known words.
If the entered word is not found in this list, it is marked as "error".

Let's try to write such a system.

The number dd of words known to us is passed to the input of the program in the first line, after which these words are
 indicated on dd lines. Then the number of ll lines of text to check is passed, after which ll lines of text.

Print unique "errors" in any order. Do your work in a case-insensitive manner.

sample input:

four
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
sample output:

stepic
champignons
the

RU
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти
слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the

"""

a = int(input())
b = []
for i in range(a):
    x = input().lower()
    if x not in b:
        b.append(x)

d = int(input())
e = []
for j in range(d):
    x = input().lower().split()
    for i in x:
        if i not in b and i not in e:
            e.append(i)

print('\n'.join(e))