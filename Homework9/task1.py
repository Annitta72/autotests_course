# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
import re

with open('test_file/task1_data.txt', encoding='utf-8') as f:
    """
    Открываем файл и в каждой строке с помощью re.sub() находим и заменяем числа на пустую строку
    """
    s = ''
    for i in f.readlines():
        s += re.sub("[0-9]", "", i)

with open('test_file/task1_answer.txt', 'w', encoding='utf-8') as f_2:
    """
    Создаем файл и записываем новую строку без чисел
    """
    f_2.write(s)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
