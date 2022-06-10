"""
EN
Download the file. It specifies the address of another file that needs to be downloaded using the requests module and
count the number of lines in it.
Use the get function to get the file (it makes sense to call the strip method on the passed parameter to strip
whitespace around the edges).
After receiving the file, you can check the result by accessing the text field. If the result of the script is not
accepted, check the url field for correctness. To count the number of lines, split the text using the splitlines method.
Enter a single number in the response field, or send a file containing a single number.

RU
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать
число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать
пробельные символы по краям).
После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не
принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода
splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.
"""
import requests

with open('task11_txt_file.txt', 'r') as inf:
    w = inf.readline().strip()
    print(w)
    r = requests.get(w)
    r = r.text.splitlines()
    print(len(r))
