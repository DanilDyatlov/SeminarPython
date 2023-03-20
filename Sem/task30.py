# Создайте список из случайных чисел. 
# Найдите второй максимум.

import random
input_list = [random.randint(1, 100) for _ in range(10)]
print(input_list)

import random
input_list = list(set([random.randint(1, 32) for _ in range(20)]))
print(input_list)
first_max = input_list[0]
second_max = input_list[1]
for i in input_list:    
    if i > first_max:       
        second_max = first_max        
        first_max = i
    elif i > second_max and i != first_max:
        second_max = i
    print(second_max)