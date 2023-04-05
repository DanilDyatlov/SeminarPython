def show_data() -> None:
    'Выводит информацию из справочника'
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read()) 


def add_data() -> None:
    'Добавляет информацию из справочника'
    fio = input ('Введите ФИО')
    tel_number = input ('Введите номер телефона')
    with open('book.txt', 'a', encoding='utf-8') as f:  #encoding='utf-8' для нормального вывода русск языка
        f.write(f'\n {fio}  |  {tel_number}') #\n перенос строки


def find_data() -> None:
    'Находит информацию из справочника'
    data = input ('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print(search(tel_book,data))


def search(book: str, info: str) -> str: #(book: str) -> str коментарий приходит строка и выводит строки для себя 
    'Находит в строке записи по определенному критерию поиска'
    book = book.split('\n')
    return '\n'.join ([post for post in book if info in post]) #join соединяет, поставили \n  поэтому соединение по ним произошло
