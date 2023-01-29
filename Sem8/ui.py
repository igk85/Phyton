from logger import delete_data, input_data, print_data, put_data


def interface():
    print('Добрый день! Это бот-помошник. \n'
    'Что вы хотите сделать? \n'
    '1. Записать данные\n'
    '2. Вывести данные\n'
    '3. Изменить данные\n'
    '4. Удалить  данные\n')

    command = int(input('Ваш выбор:'))

    while command < 1 or command > 4:
        command = int(input("Еще один шанс! Ваш выбор: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        put_data()
    else:
        delete_data()