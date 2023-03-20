# 25. Напишите программу, которая принимает на вход строку, 
# и отслеживает количество повторов каждого символа.
input_str = input("Введите строку: ")
characters_count = {}
for char in input_str:    
    if char in characters_count:    # созадается словарь, на каждый элемент строки добавляется значение, если элемент повторяется делается +1    
        characters_count[char] += 1    
    else:
        characters_count[char] = 1
print(characters_count)