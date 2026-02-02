def filter_by_state(processes: list[dict], state: str = "EXECUTED") -> list:
    """ функция принимает список словарей и опционально значение ключа
    и возвращает новый список словарей с соответствующим значением ключа """
    filtered_processes = []
    for process in processes:
        if process["state"] == state:
            filtered_processes.append(process)
    return filtered_processes


def sort_by_date(processes: list[dict], descending: bool = True) -> list:
    """ функция принимает список словарей и необязательный параметр порядка сортировки
    и возвращает отсортированный по дате список """
    sorted_processes = sorted(processes, key=lambda process: process["date"], reverse=descending)
    return sorted_processes
