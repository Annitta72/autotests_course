# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчанию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


from datetime import datetime
from time import sleep


# Здесь пишем код
def func_log(file_log='log.txt'):
    """
    Декоратор func_log, который дозаписывает в файл имя вызываемой функции, дату и время вызова

    :param file_log: входящая строка, по умолчанию равна 'log.txt' - Путь до файла

    :return: исходящая строка записи в файле
    """
    def func_dt(func):
        def wrapper():
            with open(file_log, 'a', encoding='utf-8') as f:
                f.write(f'{func.__name__} вызвана {datetime.today().strftime("%d.%m %H:%M:%S")}\n')
            func()
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper
    return func_dt


@func_log()
def func1():
    """
    1 функция
    """
    sleep(3)


@func_log(file_log='func2.txt')
def func2():
    """
    2 функция
    """
    sleep(5)


func1()
func2()
func1()
help(func1)


def func1():
    """
    1 функция
    """
    sleep(1.5)


help(func1)
