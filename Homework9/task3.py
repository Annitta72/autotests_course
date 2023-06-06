# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task3.txt') as f:
    """
    Находим сумму 3 самых дорогих покупок из файла со списком цен товара
    """
    lst_buy, buy = [], 0
    for i in f.readlines():
        if i == '\n':
            lst_buy.append(buy)
            buy = 0
            continue
        buy += int(i)
    three_most_expensive_purchases = sum((sorted(lst_buy, reverse=True))[:3])
    print('Сумма 3 самых дорогих покупок:', three_most_expensive_purchases)
assert three_most_expensive_purchases == 202346
