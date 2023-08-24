from phonebook import PhonebookEntry, save_entries_to_file, load_entries_from_file, display_entries, add_entry, edit_entry
from search import search_entries, search_entry

if __name__ == "__main__":
    entries_list = load_entries_from_file()

    while True:
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            page_size = int(input("Введите количество записей на странице: "))
            page_number = int(input("Введите номер страницы: "))
            display_entries(entries_list, page_size, page_number)

        elif choice == "2":
            new_entry = PhonebookEntry(
                input("Фамилия: "),
                input("Имя: "),
                input("Отчество: "),
                input("Название организации: "),
                input("Телефон рабочий: "),
                input("Телефон личный: ")
            )
            add_entry(entries_list, new_entry)

            print('Запись добавлена.')

        elif choice == "3":
            search_terms = dict()
            attributes_input = input("Введите атрибуты для поиска (разделяйте запятыми) или оставьте пустым. "
                                     "\nПример: 'Фамилия, Имя'. \nУказанных атрибутов должно быть не меньше трёх. ")
            if len(attributes_input.split(", ")) < 3:
                print('Вы ввели меньше трёх атрибутов для поиска.')

            else:
                if attributes_input:
                    attributes = attributes_input.split(", ")
                else:
                    attributes = PhonebookEntry.__annotations__.keys()

                for attribute in attributes:
                    value = input(f"Введите значение для атрибута '{attribute}': ")
                    search_terms[attribute] = value.capitalize()

                found_entry = search_entry(entries_list, search_terms)
                if found_entry:
                    edit_entry(entries_list, found_entry)
                    print("Запись успешно отредактирована.")

        elif choice == "4":
            search_terms = dict()

            attributes_input = input("Введите атрибуты для поиска (разделяйте запятыми) или оставьте пустым. "
                                     "\nПример: 'Фамилия, Имя'. ")
            if attributes_input:
                attributes = attributes_input.split(", ")
            else:
                attributes = PhonebookEntry.__annotations__.keys()

            for attribute in attributes:
                attribute = attribute.capitalize()
                value = input(f"Введите значение для атрибута '{attribute}': ")
                search_terms[attribute] = value

            search_results = search_entries(entries_list, search_terms)
            for result in search_results:
                print(result)

        elif choice == "5":
            print("Выход из системы.")
            break
