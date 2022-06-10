"""
EN
At some point at the Institute of Bioinformatics, biologists stopped understanding what computer scientists were saying:
 they spoke in some strange set of sounds.
At some point, one of the biologists revealed the secret of computer scientists: they used a substitution cipher when
communicating, i.e. replaced each character of the original message with its corresponding other character.
Biologists got the key to the cipher and now they need help:

Write a program that can encrypt and decrypt a substitution cipher. The program takes two strings of the same length as
input, the first line contains the characters of the source alphabet, the second line contains the characters of the
final alphabet, after which there is a string that needs to be encrypted with the passed key, and another line that
needs to be decrypted.

Let, for example, the input to the program be:
abcd
*d%#
abacabadaba
#*%*d*%

This means that the character a of the original message is replaced by the character * in the cipher, b is replaced by d, c is replaced by %, and d is replaced by #.
You need to encrypt the string abacabadaba and decrypt the string #*%*d*% using this cipher. We get the following lines, which we pass to the output of the program:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:

*d*%*d*#*d*
dacabac
Sample Input 2:

dcba
badc
dcba
badc
Sample Output 2:

badc
dcba

RU
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то
странным набором звуков.
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е.
заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь
нуждаются в помощи:
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:

*d*%*d*#*d*
dacabac
Sample Input 2:

dcba
badc
dcba
badc
Sample Output 2:

badc
dcba
"""

alph, alph_code = str(input()), str(input())
alph, alph_code = list(''.join(alph)), list(''.join(alph_code))
alph_dict = dict(zip(alph, alph_code))
in_cipher = str(input().split())
for i in in_cipher:
    if i in alph_dict:
        print(alph_dict[i], end="")

print(end="\n")

alph_dict_inverted = {value: key for key, value in alph_dict.items()}
out_cipher = str(input())
for i in out_cipher:
    print(alph_dict_inverted[i], end="")