# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1= int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))

for i in range(n):
    print(a1+(i-1)*d)

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random
# list = [random.randint(1, 20) for _ in range(10)]
# print(list)
# max_index = int(input('Введите максимальный индекс: '))
# min_index = int(input('Введите минимальный индекс: '))

# for i in range(len(list)):
#     if list[i] >= min_index and list[i] <= max_index:
#         print(f'Индекс: {i}. Значение: {list[i]}')

# def index_list(list):
#     for i in range(len(list)):
#         if list[i] >= min_index and list[i] <= max_index:
#             return list[i]
# print(index_list(i))
# print(index_list(list[i]))

# Пример решения
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)