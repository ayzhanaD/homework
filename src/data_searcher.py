import re
from collections import Counter
from typing import Any


def process_bank_search(operations: list[dict], search: str) -> list[Any] | None | Exception:
    """ функция принимает список словарей с данными о банковских операциях, строку поиска
     и возвращает список словарей, содержащих в описании данную строку """
    try:
        filtered_list = []
        for operation in operations:
            if re.search(search, operation["description"], flags=re.IGNORECASE):
                filtered_list.append(operation)

        return filtered_list

    except Exception as e:
        return e


def process_bank_operations(operations: list[dict], categories: list) -> dict | None | Exception:
    """ функция принимает список словарей с данными о банковских операциях, список категорий
     и возвращает словарь с данными о количестве данных категорий банковских операций """
    try:
        category_list = []

        for category in categories:
            for operation in operations:
                if category.lower() in operation["description"].lower():
                    category_list.append(category)

        counted = Counter(category_list)
        return counted

    except Exception as e:
        return e
