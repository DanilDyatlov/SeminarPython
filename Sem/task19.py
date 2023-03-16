# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

input_list = []
list_len = int(input("Введите количество элементов в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f"Введите число: ")))
print(input_list)
input_k = int(input("Введите число К:"))
while input_k > len(input_list):    
    input_k = input_k - len(input_list)
input_list = input_list[-input_k:] + input_list[:-input_k]
print(input_list)

# list_1 = [1, 2, 3, 4, 5]
# num = int(input())
# for i in range(num):
#     x = list_1.pop(4)
#     list_1.insert(0, x)
# print(list_1)