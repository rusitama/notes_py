class Interface:

    def __init__(self) -> None:
        self.flag = True

    def main_menu(self):
        print('\nМЕНЮ')
        print('1. Добавить заметку.\n'
              '2. Изменить заметку.\n'
              '3. Удалить заметку.\n'
              '4. Прочитать заметку по id.\n'
              '5. Просмотр всех заметок.\n'
              '0. Выход из программы.\n')

    def add_note(self):
        print('\nДобавление')

    def edit_note(self):
        print('\nДобавление')

    def read_note(self):
        print('\nЧтение')

    def delete_note(self):
        print('\nУдаление')

    def show_note(self):
        print('\nПоказать все')

    def start(self):
        while self.flag:
            self.main_menu()
            choise = input("Введите номер меню: ")
            match choise:
                case "1":
                    self.add_note()
                case "2":
                    self.edit_note()
                case "3":
                    self.delete_note()
                case "4":
                    self.read_note()
                case "5":
                    self.show_note()
                case "0":
                    self.flag = False
