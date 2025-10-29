from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_and_number: str) -> str:
    """ функция принимает строку, содержащую тип и номер карты или счета,
     и возвращает строку с замаскированным номером"""
    card_type_and_number_list = card_type_and_number.split(" ")
    card_type = ""

    for i in range(len(card_type_and_number_list) - 1):
        card_type += card_type_and_number_list[i]
        if i < len(card_type_and_number_list) - 2:
            card_type += " "

    if card_type == "Счет":
        card_number = get_mask_account(card_type_and_number_list[len(card_type_and_number_list) - 1])
    else:
        card_number = get_mask_card_number(card_type_and_number_list[len(card_type_and_number_list) - 1])

    return f"{card_type} {card_number}"


def get_date(date_str: str) -> str:
    """ функция принимает строку с датой и возвращает её в нужном формате"""
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"
