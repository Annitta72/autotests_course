# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def which_triangle(a, b, c):
    # Здесь нужно написать код
    # Выполнение условия, если стороны равны, то равносторонний
    if a == b == c:
        type_triangle = 'Равносторонний'
    # Или если любые из 2 сторон равны, то равнобедренный
    elif a == b or b == c or a == c:
        type_triangle = 'Равнобедренный'
    # Или если сумма 2 сторон больше третьей стороны, то обычный
    elif a + b > c and a + c > b and b + c > a:
        type_triangle = 'Обычный'
    # Иначе - не треугольник
    else:
        type_triangle = 'Не треугольник'
    return type_triangle

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
