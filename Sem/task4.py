# 6. Описание числа
# Пользователь вводит целое число. 
# Выведите его строку-описание вида "отрицательное четное число", "ноль", 
# "положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число".
number = int(input('Введите число: '))
if number % 2 == 0 and number < 0:
    print("отрицательное четное число")
elif number == 0:
    print("ноль")
elif number % 2 != 0 and number < 0:
    print("отрицательное нечетное число")
elif number % 2 == 0 and number > 0:
    print("положительное четное число")
else:
    print("положительное нечетное число")