"""
EN
There is a file with data on the progress of applicants. It is a set of lines, where each line contains the following information:

Surname; Grade_in_mathematics; Grade_in_physics; Grade_in_Russian_language

Fields within a row are separated by semicolons, scores are integers.

Write a program that reads a source file with a similar structure and for each applicant writes his average grade in
three subjects on a separate line corresponding to this applicant in the answer file.

Also calculate the average scores in mathematics, physics and Russian for all applicants and add the resulting values,
separated by a space, in the last line to the answer file.

As an answer to the task, attach the received file with the average marks for each student and one line with the average marks for three subjects.

Note. To split a string into parts by the character ';' you can use the split method like this:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
sample input:

Petrov;85;92;78
Sidorov;100;88;94
Ivanov;58;72;85
sample output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667

RU

Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана
следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные
значения, разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со
средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667

"""

with open('task8_txt_file.txt', encoding='utf-8') as inf:
    all_students = inf.read().strip().split('\n')
    all_students_list = [i.split(';') for i in all_students]
    num_1_lst, num_2_lst, num_3_lst, num_lst = [], [], [], []

    for lst in all_students_list:
        num_1_lst.append(lst[1])
        num_2_lst.append(lst[2])
        num_3_lst.append(lst[3])
        each_student_num_list = [int(k) for k in lst[1:]]
        each_student_medium_results = sum(each_student_num_list) / len(each_student_num_list)
        print(each_student_medium_results)
    num_1_lst_int = [int(s) for s in num_1_lst]
    num_2_lst_int, num_3_lst_int = [int(s) for s in num_2_lst], [int(s) for s in num_3_lst]

    result_1 = sum(num_1_lst_int) / len(num_1_lst_int)
    result_2 = sum(num_2_lst_int) / len(num_2_lst_int)
    result_3 = sum(num_3_lst_int) / len(num_3_lst_int)
    print(result_1, result_2, result_3)
