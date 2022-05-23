"""
EN
GC composition is an important characteristic of genomic sequences and is defined as the percentage of the sum
of all guanines and cytosines to the total number of nucleic bases in the genomic sequence.

Write a program that calculates the percentage of the characters G (guanine) and C (cytosine) in the input string
(the program should not be case-sensitive).

For example, in the string "acggtgttat" the percentage of G and C is 4/10 * 100 = 40.0
where 4 is the number of G and C characters, and 10 is the length of the string.

RU
GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение суммы
всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.

Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
(программа не должна зависеть от регистра вводимых символов).

Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10 * 100 = 40.0
где 4 -- это количество символов G и C,  а 10 -- это длина строки.


Sample Input:

acggtgttat
Sample Output:

40.0

"""

dna_str = str(input("").lower())
dna_leng = len(dna_str)
counter = 0
sum = dna_str.count("c") + dna_str.count("g")
result = sum / dna_leng * 100
print(result)