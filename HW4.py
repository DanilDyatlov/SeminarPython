# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# print('Задача №22')
# input_list1 = [] # пустой список
# list_len1 = int(input("Введите количество элементов первого набора чисел: "))
# input_list2 = [] # пустой список
# list_len2 = int(input("Введите количество элементов второго набора чисел: "))
# for i in range(list_len1):
#     input_list1.append(int(input(f"Введите число для первого набора: "))) # добавление в список чисел

# for i in range(list_len2):
#     input_list2.append(int(input(f"Введите число для второго набора: "))) # добавление в список чисел
# print()
# number_set1 = set(input_list1)
# number_set2 = set(input_list2)
# print(f'Первый набор чисел {input_list1}')
# print(f'Второй набор числе {input_list2}')
# print()
# print(f'Пересечение: {number_set1 & number_set2}') #Пересечение множеств вариант 1
# interselect = number_set1.intersection(number_set2) #Пересечение множеств вариант 2
# print(f'Пересечение: {interselect}')


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и
# с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной
# во входном файле грядки.

print('Задача №24')
count_berries = []  # пустой список
shrub_count = int(input("Введите количество кустов: "))
for i in range(shrub_count):
    # добавление в список чисел
    count_berries.append(int(input(f"Введите количество ягод на кусте: ")))
print(count_berries)
sum = list()

# for i in range(len(count_berries) - 1):
#     if i == 0:
#         sum.append(count_berries[shrub_count-1]+count_berries[i]+count_berries[i+1])
#     elif i == (shrub_count-1):
#         sum.append(count_berries[-1]+count_berries[-2]+count_berries[0])
#     else:
#         sum.append(count_berries[shrub_count-1]+count_berries[i]+count_berries[i+1])
# print(max(sum))

for i in range(len(count_berries) - 1):
    if i == (shrub_count - 1):
        sum.append(count_berries[shrub_count - 1] + count_berries[0]+count_berries[1])
    elif i == (shrub_count - 2):
        sum.append(count_berries[shrub_count - 1] + count_berries[shrub_count - 2] + count_berries[0])
    else:
        sum.append(count_berries[i + 2] + count_berries[i] + count_berries[i + 1])
# print(max(f' Максимальное количесвтво ягод которое можно собрать: {sum} '))
print(max(sum))
