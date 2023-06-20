def load_contacts(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            contact_data = line.strip().split(',')
            contact = {
                'Фамилия': contact_data[0],
                'Имя': contact_data[1],
                'Отчество': contact_data[2],
                'Номер телефона': contact_data[3]
            }
            contacts.append(contact)
    return contacts


def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            line = ','.join([
                contact['Фамилия'],
                contact['Имя'],
                contact['Отчество'],
                contact['Номер телефона']
            ])
            file.write(line + '\n')


def search_contacts(contacts, key, value):
    result = []
    for contact in contacts:
        if contact[key] == value:
            result.append(contact)
    return result


def add_contact(contacts):
    Фамилия = input('Введите фамилию: ')
    Имя = input('Введите имя: ')
    Отчество = input('Введите отчество: ')
    Номер_телефона = input('Введите номер телефона: ')

    contact = {
        'Фамилия': Фамилия,
        'Имя': Имя,
        'Отчество': Отчество,
        'Номер телефона': Номер_телефона
    }

    contacts.append(contact)


def edit_contact(contacts):
    Фамилия_или_имя = input('Введите фамилию или имя для редактирования: ')
    found_contacts = search_contacts(contacts, 'Фамилия', Фамилия_или_имя)
    found_contacts.extend(search_contacts(contacts, 'Имя', Фамилия_или_имя))

    if len(found_contacts) == 0:
        print('Контакт не найден.')
        return

    print('Найденные контакты:')
    for index, contact in enumerate(found_contacts):
        print(f"{index + 1}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']} {contact['Номер телефона']}")

    contact_index = int(input('Введите номер контакта для редактирования: ')) - 1

    if contact_index < 0 or contact_index >= len(found_contacts):
        print('Неверный номер контакта.')
        return

    contact = found_contacts[contact_index]

    Фамилия = input('Введите новую фамилию (оставьте пустым, если не хотите менять): ')
    Имя = input('Введите новое имя (оставьте пустым, если не хотите менять): ')
    Отчество = input('Введите новое отчество (оставьте пустым, если не хотите менять): ')
    Номер_телефона = input('Введите новый номер телефона (оставьте пустым, если не хотите менять): ')

    if Фамилия:
        contact['Фамилия'] = Фамилия
    if Имя:
        contact['Имя'] = Имя
    if Отчество:
        contact['Отчество'] = Отчество
    if Номер_телефона:
        contact['Номер телефона'] = Номер_телефона


def delete_contact(contacts):
    Фамилия_или_имя = input('Введите фамилию или имя для удаления: ')
    found_contacts = search_contacts(contacts, 'Фамилия', Фамилия_или_имя)
    found_contacts.extend(search_contacts(contacts, 'Имя', Фамилия_или_имя))

    if len(found_contacts) == 0:
        print('Контакт не найден.')
        return

    print('Найденные контакты:')
    for index, contact in enumerate(found_contacts):
        print(f"{index + 1}. {contact['Фамилия']} {contact['Имя']} {contact['Отчество']} {contact['Номер телефона']}")

    contact_index = int(input('Введите номер контакта для удаления: ')) - 1

    if contact_index < 0 or contact_index >= len(found_contacts):
        print('Неверный номер контакта.')
        return

    contact = found_contacts[contact_index]
    contacts.remove(contact)


def print_contacts(contacts):
    if len(contacts) == 0:
        print('Справочник пуст.')
        return

    for contact in contacts:
        print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']} {contact['Номер телефона']}")


def main():
    filename = 'contacts.txt'
    contacts = load_contacts(filename)

    while True:
        print('--- Телефонный справочник ---')
        print('1. Вывести контакты')
        print('2. Добавить контакт')
        print('3. Редактировать контакт')
        print('4. Удалить контакт')
        print('5. Сохранить и выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            print_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(filename, contacts)
            print('Контакты сохранены в файл.')
            break
        else:
            print('Неверный выбор. Пожалуйста, повторите.')

        print()

if __name__ == '__main__':
    main()
