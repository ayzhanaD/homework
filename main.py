# функция для фильтрации операций по определенному слову
from src.data_searcher import process_bank_search
# функции для чтения CSV-файлов и Excel-файлов
from src.file_reader import read_csv_file, read_excel_file
# функция для вывода операций только в рублях
from src.generators import filter_by_currency
# функции для фильтрации по статусу и по дате
from src.processing import filter_by_state, sort_by_date
# функции для чтения JSON-файлов
from src.utils import get_transactions
# функции для получения форматированной даты и маскировки номеров счетов
from src.widget import get_date, mask_account_card


def main():
    """ функция отвечает за основную логику программы и связывает функциональности между собой """

    # тип файла для чтения
    while True:
        file_type = input(
            "\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "\n1. Получить информацию о транзакциях из JSON-файла"
            "\n2. Получить информацию о транзакциях из CSV-файла"
            "\n3. Получить информацию о транзакциях из XLSX-файла\n\n"
        )

        if file_type == "1":
            print("Для обработки выбран JSON-файл")
            data = get_transactions("data/operations.json")
            break
        elif file_type == "2":
            print("Для обработки выбран CSV-файл")
            data = read_csv_file("data/transactions.csv")
            break
        elif file_type == "3":
            print("Для обработки выбран XLSX-файл")
            data = read_excel_file("data/transactions_excel.xlsx")
            break

    # статус фильтрации данных
    while True:
        state = input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию."
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\n"
        ).lower()

        if state == "executed":
            data = filter_by_state(data, state)
            break
        elif state == "canceled":
            data = filter_by_state(data, state)
            break
        elif state == "pending":
            data = filter_by_state(data, state)
            break
        else:
            print(f"\nСтатус операции '{state.upper()}' недоступен")

    print(f"Операции отфильтрованы по статусу '{state.upper()}'\n")

    # ВЫБОРКА
    count = 0

    # сортировка по дате
    is_sorted_by_date = input("\nОтсортировать операции по дате? Да/Нет\n").lower().strip()
    if is_sorted_by_date == "да":
        asc_or_desc = input("\nОтсортировать по возрастанию или по убыванию\n").lower().strip()
        if asc_or_desc == "по возрастанию":
            data = sort_by_date(data, False)
            count += 1
        else:
            data = sort_by_date(data, True)
            count += 1
    elif is_sorted_by_date == "нет":
        count += 1

    # только рубли
    is_only_rub = input("\nВыводить только рублевые транзакции? Да/Нет\n").lower().strip()
    if is_only_rub == "да":
        data = list(filter_by_currency(data, "RUB"))
        count += 1
    elif is_only_rub == "нет":
        count += 1

    # фильтрация по слову
    is_filtered_by_re = input("\nОтфильтровать список транзакций "
                              "по определенному слову в описании? Да/Нет\n").lower().strip()
    if is_filtered_by_re == "да":
        user_search = input("Введите слово для поиска: ").lower().strip()
        data = process_bank_search(data, user_search)
        count += 1
    elif is_filtered_by_re == "нет":
        count += 1

    # ВЫВОД
    if count > 0 and len(data) > 0:
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {count}")

        for row in data:
            # дата и описание
            print(f"\n{get_date(row["date"])} {row["description"]}")

            # маска номеров
            try:
                print(f"{mask_account_card(row["from"])} -> {mask_account_card(row["to"])}")
            except KeyError:
                print(f"{mask_account_card(row["to"])}")

            # сумма
            try:
                print(f"{row["amount"]} {row["currency_code"]}")
            except KeyError:
                print(f"{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["code"]}")

    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")


main()
