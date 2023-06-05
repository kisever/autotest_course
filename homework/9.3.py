# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task_3.txt') as f:
    data = f.read().split()

# создаем список списков товаров (все товары на одной покупке в одном подсписке)
purchases = []
temp = []
for d in data:
    if d == '':
        if temp:  # если временный список не пустой, добавляем его в список покупок
            purchases.append(temp)
            temp = []  # очищаем временный список
    else:
        temp.append(d)

# преобразуем все цены товаров в числа
purchases = list(map(lambda x: [float(i) for i in x], purchases))

# создаем список всех цен
prices = []
for purchase in purchases:
    prices += purchase

# находим сумму трех самых дорогих покупок
sorted_prices = sorted(prices, reverse=True)
three_most_expensive_purchases = sum(sorted_prices[:3])

assert three_most_expensive_purchases == 202346