# Создайте список из случайных чисел. 
# Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, 
# который больше любого из своих соседей).
import random
input_list = [random.randint(1, 100) for _ in range(10)]
print(input_list)
for i in range(len(input_list) - 2, 0, -1):
    if input_list[i - 1] < input_list[i] > input_list[i + 1]:        
        print(i)        
        break