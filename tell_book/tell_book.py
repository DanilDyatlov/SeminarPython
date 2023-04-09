
# with open('book.txt', 'w', encoding = 'utf-8') as f:
# # w все данные удаляются и перезаписывается
# # а дополняется в документ 
# # r чтение
#     f.write('фио |  номер телефона')
    
# with open('book.txt', 'a', encoding='utf-8') as f:
#     f.write('\n фио |  номер телефона1')

# with open('book.txt', 'r', encoding='utf-8') as f:
#   print(f.read()) 
# # \n или endline с новой строки запись 

import tell_book_function


while True:
    print('Выберите действие: 1. вывод, 2. добавление, 3. поиск, 4. изменить, 5. удалить')
    mode = int(input())
    if mode == 1:
        tell_book_function.show_data()
    elif mode == 2:
        tell_book_function.add_data()
    elif mode == 3:
        tell_book_function.find_data()
    elif mode == 4:
        tell_book_function.change_data()
    elif mode == 5:
        tell_book_function.delete_data()
    else:
        break
