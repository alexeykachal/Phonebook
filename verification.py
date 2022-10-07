
import controller as c


def verify_int_number(number):
    '''
    Проверка является ли число целым
    '''
    while True:
        try:
            return int(input(number))
        except ValueError:
            print("Введено не целое число")

def verify_number_double(number):
    '''
    Проверка нет ли больше такого номера, если есть - выходим
    '''
    with open('phonebook.csv', 'r', encoding='UTF-8') as file:
        a = file.readlines()
        for i in a:
            if int((i.split(",")[2])) == int(number):
                print("такой номер уже есть в списке, добавьте другой контакт")
                quit()


def verify_choice(choice):
    '''
    Проверка выбора операции
    '''
    while True:
        try:
            menu_choice = int(input(choice))
            if menu_choice in range(1,7):
                return menu_choice
            else:
                list_options = ["Меню справочника:", "1 - добавить контакт", "2 - удалить контакт", "3 - поиск контакта",
                    "4 - экспортировать контакты","5 - показать книгу контактов", "6 - выход из справочника"]
                print(*list_options, sep ='\n')
        except ValueError:
            print('Вы ввели не число')

def verify_letter(letter):
    '''
    Проверка на отсутствие чисел и прочих знаков
    '''
    while True:
        letter_choice = input(letter)
        if letter_choice.isalpha() == True:
            return letter_choice.title()
        else:
            print("Введены не только буквы!")

def verify_des_input(des):
    '''
    Проверка на длину описания
    '''
    while True:
        description = input(des)
        if len(description) <= 17:
            return description
        else:
            print("Описание должно быть не длиннее 17 символов")

def verify_exit(choice):
    '''
    Проверка выбора операции
    '''
    while True:
        try:
            leave = int(input(choice))
            if leave == 1:
                return c.button_click()
            else:
                print("Вы ввели не единицу")
        except ValueError:
            print('Вы ввели не число')


