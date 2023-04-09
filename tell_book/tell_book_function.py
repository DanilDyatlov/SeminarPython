def show_data() -> None:
    'Выводит информацию из справочника'
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read()) 


def add_data() -> None:
    'Добавляет информацию из справочника'
    fio = input ('Введите ФИО: ')
    tel_number = input ('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:  #encoding='utf-8' для нормального вывода русск языка
        f.write(f'\n{fio}  |  {tel_number}') #\n перенос строки. Происходит запись каждый раз с новой строки 


def find_data() -> None:
    'Находит информацию из справочника'
    data = input ('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read() # для работы дальнейшей нам нужно прочитать все информацию 
    print('Результат поиска: ')
    print(search(tel_book,data)) 
    # ппринимает базу данных  tel_book и параметр поиска data


def search(book: str, info: str) -> str: #(book: str) -> str коментарий приходит строка и выводит строки для себя 
    'Находит в строке записи по определенному критерию поиска'
    book = book.split('\n') 
    # база данных состоит из одной большой строки, для этого мы ее разделяем по переносу строки \n переход на новую строку  
    return '\n'.join ([post for post in book if info in post]) #join соединяет, поставили \n  поэтому соединение по ним произошло
    # post  это запись из book если info находить в записи post. Если мы нашли такое соответсвие то добавляем. 
    # когда нашли выводим с помощью join


def changing(text: str) -> str:
    '''Вносит изменения'''
    fio = input('Внесите новые данные ФИО (enter для пропуска): ')
    tel_num = input('Введите новый номер тел (enter для пропуска): ')
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(tel_num) == 0:
        tel_num = text.split(' | ')[1]
    return (f'{fio} | {tel_num}')

# def changing:
# а = ['Влад | +789', 'Анна | +798']
# b = 'Влад | +789'
# a[a.index(b)] = changing(b)
# print(a)

#    

def change_data() -> None:
    'Ищем по значению все данные из справочника и вносим изменения в нужное'
    find = input('Введите данные для поиска изменяемого контакта: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    result = search(tel_book, find)
    print(result)
    
    tel_book = tel_book.split('\n') 
    # разделяем все с новой строки
    tel_book[tel_book.index(result)] = changing(result)
    #tel_book с индексом tel_book.index(result) изменяем на result  после изменения 

    with open('book.txt', 'w', encoding='utf-8') as f:
        for item in tel_book: 
            f.write(f'\n{item}')
    #после изменения идет запись новых данных 

def delete_data() -> None:
    delet = input('Поиск контакта для удаления: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    result = search(tel_book, delet)
    print(result)

    tel_book = tel_book.split('\n')
    tel_book.remove(result)
    
    with open('book.txt', 'w', encoding='utf-8') as f:
        for item in tel_book: 
            f.write(f'\n{item}')