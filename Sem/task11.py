# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое
# число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

input_number = int(input("Введите натуральное число: "))
first_fibonachi = 0 # число 0 и 1 задаются так как они начальные
second_fibonachi = 1
tmp_fibonachi = first_fibonachi + second_fibonachi #третье число, сумма двух предидущих
index = 2 # счетчик 
while tmp_fibonachi < input_number:
    first_fibonachi = second_fibonachi # firs = 1 1 2
    second_fibonachi = tmp_fibonachi # second = 1 2 3
    tmp_fibonachi = first_fibonachi + second_fibonachi # tmp = 2 3 5 происходит перепесь значений для фибоначчи 
    index += 1
if tmp_fibonachi == input_number:
    print(index + 1)
else:
    print(-1)