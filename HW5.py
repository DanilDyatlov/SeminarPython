# Задача 6. Дана строка (возможно, пустая),состоящая из букв A-Z
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB

# Нужно написать функцию RLE, которая на выходе даст строку вида

# A4B3C2XYZD4E3F3A6B2

# И сгенерирует ошибку , если на вход пришла невалидная строка.
# Пояснения : Если символ встречается 1 раз , он остается без изменений ; 
# Если символ повторяется более 1 раза , к нему добавляется количество повторений

# def rle(input_str):
#     result = [] #сюда будем записывать рузельтат, но пока он пустой 
#     count_sumbol = 1 #число 1 так как начинаем с первого числа и 1 уже у нас есть 
#     current_sumbol = input_str[0] # первый символ запоминаем первую букву 
#     input_str += ' ' # чтобы последняя буква попала
#     for ind in range(1,len(input_str)): #проходимся по всей длине по индексам 
#         if current_sumbol == input_str[ind]: # если первое число равно последующему накручиваем счетчик
#             count_sumbol +=1 #счетчик
#         else: #когда последовательность прерывается переходим на другую букву
#             if count_sumbol == 1: #доп условие если буква всего лишь одна 
#                 result.append(f'{current_sumbol}') #добавление буквы в результат 
#             else:
#                 result.append(f'{current_sumbol}{count_sumbol}') # если буква не одна то добавляем саму букву и его счетчик
#             count_sumbol = 1
#             current_sumbol = input_str[ind] #переходим на другую букву 
#     return result
#     # print(*result, sep="")

# # rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
# input_str = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
# print(*rle(input_str), sep="")

# Задача 3 
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"

# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] 
 
# Т.е. сгруппировать слова по"общим буквам"
# Пример
# def group_letter(input_list):
#     word_dict = {}
#     for word in input_list:
#         if (frozenset(word), len(word)) not in word_dict:
#             word_dict[(frozenset(word), len(word))] = [word]
#         else:
#             word_dict[(frozenset(word), len(word))].append(word)
#     res_list = []
#     for value in word_dict.values():
#         res_list.append(value)
#     return res_list

# print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat", 'batt', 'b', 'cadfsdf']))


def groups_letters (input_list):
    groups_of_words = {} # создаем словарь
    for word in input_list: # проходим по списку 
        if (frozenset(word), len(word)) not in groups_of_words: 
            # если такого множества с длиной нет в словаре то добавляем
            # в качестве ключа юудет множество букв из слова и его длина
            # получаем картеж ключа  
            groups_of_words[(frozenset(word), len(word))] = [word] 
            # в качесвте ключей словаря неизменяемы данные поэтому фрозен. Добавляем ключ из множества с длинной и значение 
        else:
            groups_of_words[(frozenset(word), len(word))].append(word)
            # если такой ключ со значением есть то добавляю туда слово ко множеству 
    groups_of_words = list(groups_of_words.values())
    return groups_of_words

input_list = "eat", "tea", "tan", "ate", "nat", "bat", "batt", "b"
print(groups_letters(input_list))

# d = set("eat") разбивает по буквам
# print(d)