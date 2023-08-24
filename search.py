from typing import List, Dict, Union
from phonebook import PhonebookEntry


def search_entries(entries: List[PhonebookEntry], search_terms: Dict[str, str]) -> List[PhonebookEntry]:
    """Поиск по определеннмы атрибутам.
    Код распознает как названия атрибутов класса, так и их значения в разных регистрах.

    """
    results = []
    for entry in entries:
        fact_true = all(
            hasattr(entry, key.replace(" ", "_"))
            and getattr(entry, key.replace(" ", "_")).lower() == value.lower()
            for key, value in search_terms.items()
        )
        if fact_true:
            results.append(entry)
    return results


def search_entry(entries: List[PhonebookEntry], search_terms: Dict[str, str]) -> Union[PhonebookEntry, None]:
    """Метод предназначается для редактирования записи. В отличии от метода выше, метод находит только одну запись."""
    for entry in entries:
        fact_true = all(
            hasattr(entry, key.replace(" ", "_"))
            and getattr(entry, key.replace(" ", "_")).lower() == value.lower()
            for key, value in search_terms.items()
        )

        if fact_true:
            return entry
    return None
