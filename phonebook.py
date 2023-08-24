from dataclasses import dataclass, asdict
from typing import List, Dict, Union
import json


@dataclass
class PhonebookEntry:
    Фамилия: str
    Имя: str
    Отчество: str
    Название_организации: str
    Рабочий_телефон: str
    Личный_телефон: str


def save_entries_to_file(entries: List[PhonebookEntry]) -> None:
    """Сохранение записей из справочника"""
    with open("phonebook.json", "w", encoding="utf-8") as file:
        json.dump([asdict(entry) for entry in entries], file, ensure_ascii=False, indent=4)


def load_entries_from_file() -> List[PhonebookEntry]:
    """Загрузка записей из справочника. Использовал контекстный менеджер для автомататического закрытия"""
    try:
        with open("phonebook.json", "r", encoding="utf-8") as file:
            entries_data = json.load(file)
            entries = [PhonebookEntry(**entry_data) for entry_data in entries_data]
            return entries
    except FileNotFoundError:
        return []


def display_entries(entries: List[PhonebookEntry], page_size: int, page_number: int) -> None:
    """Вывод записей, согласно заданию: вывод постранично записей на экран.
    start_idx и end_idx необходимы для отображения опредленного количества записей на странице."""
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    for entry in entries[start_idx:end_idx]:
        print(entry)


def add_entry(entries: List[PhonebookEntry], new_entry: PhonebookEntry) -> None:
    """Добавление контакта в справочник"""
    if not new_entry.Фамилия or not new_entry.Имя or not new_entry.Отчество:
        print("Ошибка: Фамилия, имя и отчество обязательные атрибуты для заполнения.")
        return
    entries.append(new_entry)
    save_entries_to_file(entries)


def edit_entry(entries: List[PhonebookEntry], found_entry: PhonebookEntry) -> None:
    print('Редакция записи')
    """Редактирование записи - индекс персого контакта начинается с 0"""
    updated_entry = PhonebookEntry(
        input(f"Фамилия ({found_entry.Фамилия}): ") or found_entry.Фамилия,
        input(f"Имя ({found_entry.Имя}): ") or found_entry.Имя,
        input(f"Отчество ({found_entry.Отчество}): ") or found_entry.Отчество,
        input(f"Название организации ({found_entry.Название_организации}): ") or found_entry.Название_организации,
        input(f"Телефон рабочий ({found_entry.Рабочий_телефон}): ") or found_entry.Рабочий_телефон,
        input(f"Телефон личный ({found_entry.Личный_телефон}): ") or found_entry.Личный_телефон
    )
    entries[entries.index(found_entry)] = updated_entry
    save_entries_to_file(entries)
