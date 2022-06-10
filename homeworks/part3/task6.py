"""
EN
Last week we compressed strings using repetition encoding. Now our task will be to restore the original string back.

Write a program that reads from a file a line corresponding to the text compressed using repetition coding and performs
the reverse operation, obtaining the original text.

Write the received text to a file and attach it as an answer to this task.
There are no numbers in the source text, so the code is uniquely interpretable. N
ote. This is the first Dataset Quiz. In such tasks, after clicking "Start Quiz" you will see a link "download your
dataset". Use this link to download the input file to your computer. Run your program using this file as input.
The output file that you get from this should be sent as an answer to this task.

RU
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной
строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка
"download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас
получится, надо отправить в качестве ответа на эту задачу.

Sample Input:

a3b4c2e10b1

Sample Output:

aaabbbbcceeeeeeeeeeb
"""
alph_list = []
num_string = ' '
num_list = []
result = []
with open('task6_txt_file.txt') as inf:
    for line in inf:
        line = line.strip()
        for i in line:
            if i.isalpha():
                alph_list.append(i)
                num_string += ' '
            else:
                num_string += i

            int_list = []
            num_list = list(filter(lambda x: x.isdigit(), num_string.split(' ')))

            for item in num_list:
                int_list.append(int(item))

result = list(map(lambda i, j: i * j, alph_list, int_list))

result = ''.join(result)
print(result)