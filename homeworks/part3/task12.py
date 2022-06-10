"""
EN
There is a set of files, each of which, except for the last one, contains the name of the next file.
The first word in the text of the last file: "We".

Download the suggested file. It contains a link to the first file from this set.

All files are located in the directory at:
https://stepic.org/media/attachments/course67/3.6.3/

Download the contents of the last file from the set as an answer to this challenge.

RU
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""
import requests

with open('task12_txt_file.txt', 'r') as inf:
    w = inf.readline().strip()
    print(w)
    r = requests.get(w)

    while True:
        if not r.text.startswith('We'):
            r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
            print(r.text)
        else:
            print(r.text)
            break