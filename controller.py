import UI as ui

def button_click():
    '''
    Начало ввода данных
    '''
    list_options = ["Меню справочника:", "1 - добавить контакт", "2 - удалить контакт", "3 - поиск контакта",
                    "4 - экспортировать контакты","5 - показать книгу контактов", "6 - выход из справочника"]
    print(*list_options, sep='\n')
    choice = ui.calc_choice()

    if choice == 1:
        #Контакты вводятся только числами! если нужен код другой страны добавляем в описание информацию.
        #Поле описание обязательно заполняем, можно просто ставить "-"
        #Два контакта с одним номером не даст ввести!
        ui.data_input()

    elif choice == 2:
        #Удаляем контакт - удаляем по уникальному ключу - номеру телефона
        ui.contact_del()

    elif choice == 3:
        #Ищем контакт по четкому совпадению ФИО
        ui.contact_find()

    elif choice == 4:
        #Экспортируем в JSON
        ui.json_export()

    elif choice == 5:
        #Просмотр нашей книги контактов
        print("Для выхода в главное меню нажимите - 1")
        ui.show_book()
        ui.book_exit()

    elif choice == 6:
        # Прерываем программу
        quit()