# Напишите алгоритм, который берет список lst и перемещает все нули в конец, сохраняя порядок остальных элементов.
# Например (Ввод --> Вывод) :
# [1, 0, 1, 2, 0, 1, 3]  => [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    # Здесь нужно написать код
    x = lst.count(0)  # Находим кол-во 0 в списке
    lst = list(filter(None, lst))  # Удаление 0 функцией filter() в списке
    lst.extend([0] * x)  # Добавление в кол-ве всех найденных 0 в конец списка
    return lst

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 0, 1, 0, 1, 0, 3, 0, 1],
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
    [0, 0],
    [1, 9, 5, 4, 8, 2],
    []
]

test_data = [
    [1, 2, 1, 1, 3, 1, 0, 0, 0, 0],
    [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0],
    [1, 9, 5, 4, 8, 2],
    []
]


for i, d in enumerate(data):
    assert move_zeros(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
