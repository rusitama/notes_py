# Приложение заметки
# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.

def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Просмотр записей.\n'
              '2. Добавить новую запись.\n'
              '3. Изменить существующую запись.\n'
              '4. Экспорт записей.\n'
              '5. Импорт записей.\n'
              '6. Удалить запись.\n'
              '7. Поиск записей.\n'
              '8. Выход из программы.\n')

        n = check_for_number(input('Выберите пункт меню: '))

        if n == 1:
            print(db.serch())
        elif n == 2:
            name = input('Введите имя: ')
            while True:
                if name == "":
                    name = input('Имя не может быть пустым. Введите имя повторно: ')
                if name != "":
                    break
            surname = input('Введите фамилию: ')
            while True:
                if surname == "":
                    surname = input('Фамилие не может быть пустым. Введите фамилию повторно: ')
                if surname != "":
                    break
            number = input('Введите номер телефона: ')
            while True:
                if number == "":
                    number = input('Номер не может быть пустым. Введите номер повторно: ')
                if number != "":
                    break
            db.create(name, surname, number)
        elif n == 3:
            print('1. Найти номер по фамилии.\n'
                  '2. Найти номер по имени.\n'
                  '3. Поиск по номеру телефона.\n')
            change = check_for_number(input('Введите номер пункта: '))
            if change == 1:
                search = input('Введите фамилию: ')
                db.serch(surname=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                db.update(id=user_id, new_number=new_number)
            elif change == 2:
                search = input('Введите имя: ')
                db.serch(name = search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                db.update(id = user_id, new_number = new_number)
            elif change == 3:
                search = input('Введите номер телефона: ')
                db.serch(number = search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                db.update(id = user_id, new_number = new_number)
            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
        elif n == 4:
            print('1. Экспортировать в XML файл.\n'
                  '2. Экспортировать в TXT файл.\n')
            export = check_for_number(input('Введите номер пункта: '))
            if export == 1:
                db.export_data_to_xml()
            elif export == 2:
                db.export_data_to_txt()
            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
        elif n == 5:
            print('1. Экспортировать в XML файл.\n'
                  '2. Экспортировать в TXT файл.\n')
            export = check_for_number(input('Введите номер пункта: '))
            if export == 1:
                db.parse_xml()
            elif export == 2:
                db.import_from_txt()
            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
        elif n == 6:
            print('1. Найти номер по фамилии.\n'
                  '2. Найти номер по имени.\n'
                  '3. Поиск по номеру телефона.\n')
            deleting = check_for_number(input('Введите номер пункта: '))
            if deleting == 1:
                search = input('Введите фамилию: ')
                print(db.serch(surname = search))
                user_id = input('Введите id записи: ')
                db.delete(id = user_id)
            elif deleting == 2:
                search = input('Введите имя: ')
                print(db.serch(name = search))
                user_id = input('Введите id записи: ')
                db.delete(id = user_id)
            elif deleting == 3:
                search = input('Введите номер телефона: ')
                print(db.serch(number = search))
                user_id = input('Введите id записи: ')
                # new_number = input('Введите новый номер телефона: ')
                db.delete(id = user_id)
            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
        elif n == 7:
            search = input('Введите номер  телефона: ')
            print(db.serch(number=search))

            #search = input('Введите фамилию: ')
            #print(db.serch(surname=search))
        elif n == 8:
            print('Завершение.')
            break
        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def check_for_number(n):
    while not n.isdigit():
        print('\nВведенный значение не является числом.')
        n = input('Введите повторно значение меню: ')
    return int(n)

menu();