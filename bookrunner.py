import csv

def bookfiller(full_contact):
    """
    Заводим данные в книжку контактов
    """
    with open('phonebook.csv', 'a', encoding = 'UTF-8') as file:
        write = csv.writer(file, delimiter = ",", lineterminator="\r")
        write.writerow(full_contact)
    file.close()