# 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

input_number = int(input("Введите число N: "))
factorial = 1
while input_number > 0:   # 8 7 6 5 4
    factorial *= input_number
    input_number -= 1
print(factorial)