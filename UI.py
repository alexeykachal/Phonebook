
import bookrunner as b
import verification as v
import csv
import json
import controller as c
import os

def calc_choice():
    '''
    Выбор калькулятора
    '''
    choice = f'Введите нужный пункт меню: '
    return v.verify_choice(choice)

def data_input():

    data_dictionary = {}

    def name_choice():
        '''
        Ввод имени контакта
        '''
        name = f'Введите имя: '
        return v.verify_letter(name)

    def surname_choice():
        '''
        Ввод фамилии контакта
        '''
        surname = f'Введите фамилию: '
        return v.verify_letter(surname)

    def number_choice():
        '''
        Ввод номера контакта
        '''
        number = f'Введите номер телефона: '
        return v.verify_int_number(number)

    def des_input():
        '''
        Ввод описания контакта до 17 символов
        '''
        description = f'Введите описание контакта: '
        return v.verify_des_input(description)

    new_contact_name = name_choice()
    new_contact_surname = surname_choice()
    new_contact_number = number_choice()
    new_contact_des = des_input()
    v.verify_number_double(new_contact_number)

    full_contact = [new_contact_name,new_contact_surname,new_contact_number,new_contact_des]

    b.bookfiller(full_contact)

    print("Контакт добавлен в книгу")
    c.button_click()

def show_book():
    print("Имя / Фамилия / Номер / Описание - Телефонная книга")
    with open('phonebook.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for line in reader:
            line = ' '.join(line)
            print(line)

def book_exit():
    '''
    Выбор калькулятора
    '''
    choice = f'Для выхода введите один здесь единицу: '
    return v.verify_exit(choice)

def contact_del():
    '''
    Удаляем контакт
    '''
    number_del = input("Введите номер контакта который нужно удалить: ")
    with open('phonebook.csv', 'r', encoding='UTF-8') as file:
        a = csv.reader(file)
        for i in a:
            if int((i[2])) != int(number_del):
                with open('try.csv', 'a', encoding='UTF-8', newline='') as f:
                    write = csv.writer(f)
                    write.writerow(i)

        file.close()
        os.remove('phonebook.csv')
        os.rename('try.csv', "phonebook.csv")
        c.button_click()
        print("Контакт удален")

    '''
    Ищем контакт по точному совпадению ФИО - может отобразиться несколько контактов
    '''
    def name_choice():
        '''
        Ввод имени контакта
        '''
        name = f'Введите имя: '
        return v.verify_letter(name)

    def surname_choice():
        '''
        Ввод фамилии контакта
        '''
        surname = f'Введите фамилию: '
        return v.verify_letter(surname)

    find_contact_name = name_choice()
    find_contact_surname = surname_choice()

    with open('phonebook.csv', 'r', encoding='UTF-8') as file:
        a = csv.reader(file)
        count = 0
        z = []
        for i in a:
            if i[0] == find_contact_name and i[1] == find_contact_surname:
                count += 1
                z.append(i)
        if count > 0:
            for i in z:
                print(f'Имя:{i[0]}, Фамилия: {i[1]}, Номер: {i[2]}, Описание: {i[3]}')
            file.close()

        else:
            print("такого контакта нет")


def json_export():

    with open('phonebook.csv', 'r', encoding = 'UTF-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        print(rows)
    with open('export.json', 'w', encoding = 'UTF-8') as f:
        json.dump(rows, f)
    print("Экспорт завершен")
    c.button_click()
    file.close()