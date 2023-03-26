# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

# 0, 1, 1, 2, 3, 5, 8, 13...
def fibonachi_recursion(serial_number):
    if serial_number == 1:
        return 0
    if serial_number == 2:
        return 1    
    return fibonachi_recursion(serial_number - 1) + fibonachi_recursion(serial_number - 2)

def fibonachi_iteration(serial_number):
    first = 0    
    second = 1    
    if serial_number == 1:        
        return first    
    if serial_number == 2:        
        return second    
    count = 2    
    while serial_number != count:
        third = first + second
        first = second
        second = third
        count += 1
        return third
print(fibonachi_recursion(15))
print(fibonachi_iteration(15))