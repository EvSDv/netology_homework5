# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    def get_list_files():
        files_list = filter(lambda x: x.endswith('.sql'), os.listdir(os.path.join(current_dir, migrations)))
        return list(files_list)

    def search_in_files(search_line, file_list_to_search):
        total = 0
        file_list = []
        for file in file_list_to_search:
            with open(os.path.join(current_dir, migrations, file)) as f:
                if search_line.lower() in f.read().lower():
                    file_list.append(file)
                    print(file)
                    total += 1
        print('Всего:', total)
        return file_list

    def main(file_list_to_search):
        search_line = input('Введите строку поиска \n')
        new_list = search_in_files(search_line, file_list_to_search)
        main(new_list)


    main(get_list_files())

