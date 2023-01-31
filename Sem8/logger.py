from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 Вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 Вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варината: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('Sem8\data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('Sem8\data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('Успешно!!')



def print_data(file_number = None):
    if file_number is None or file_number == 1:
        print('1 файл:')
        with open('Sem8\data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            data_first = file.readlines()
            data_first_second = []
            j = 0
            num = 1
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_second.extend([f"\n{num}.\n", ''.join(data_first[j:i]).strip(), '\n'])
                    j = i
                    num += 1
            data_first = data_first_second
            print(''.join(data_first))
    
    if file_number is None or file_number == 2:
        print('2 файл:\n')
        with open('Sem8\data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            data_second = list(file.readlines())
            num = 1
            for i in data_second:
                if i != '\n':
                    i = i.strip()
                    print(f'{num}. {i}')
                    num += 1    




def put_data():
    file_num = int(input(f'Укажите какой файл Вы хотите изменить:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))
    
    if file_num != 1 and file_num != 2:
        file_num = int(input(f'Укажите какой файл Вы хотите изменить:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))

    if file_num == 1:
        print_data(1)
        with open('Sem8\data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите изменить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    new_book.extend([name_data() + '\n', surname_data() + '\n', phone_data() + '\n', adress_data() + '\n', '\n'])
                    counter += 1
                    i += 5

        with open('Sem8\data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)
    
    if file_num == 2:
        print_data(2)
        with open('Sem8\data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите изменить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    new_book.append(f'{name_data()};{surname_data()};{phone_data()};{adress_data()}\n')
                    counter += 1
                    i += 1
        
        with open('Sem8\data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)


def delete_data():
    file_num = int(input(f'Укажите в каком файле Вы хотите удалить запись:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))
    
    if file_num != 1 and file_num != 2:
        file_num = int(input(f'Укажите в каком файле Вы хотите удалить запись:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))

    if file_num == 1:
        print_data(1)
        with open('Sem8\data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите удалить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    counter += 1
                    i += 5
                
        with open('Sem8\data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)

    if file_num == 2:
        print_data(2)
        with open('Sem8\data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите удалить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    counter += 1
                    i += 2
            
        with open('Sem8\data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)
