def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number (str): Номер карты в виде строки.

    Returns:
        str: Замаскированный номер карты.
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (str): Номер счета в виде строки.

    Returns:
        str: Замаскированный номер счета.
    """
    return f"**{account_number[-4:]}"

# Пример использования функций:

card_num = "7000792289606361"
account_num = "73654108430135874305"

print(get_mask_card_number(card_num))  # Вывод: 7000 79** **** 6361
print(get_mask_account(account_num))   # Вывод: **4305

from datetime import datetime
def get_date(date_str):
    """
    Преобразует строку с датой из формата "YYYY-MM-DDTHH:MM:SS.ssssss" в формат "ДД.ММ.ГГГГ".
    Args:
        date_str (str): Строка с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss".
    Returns:
        str: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    # Парсим строку с датой в объект datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Преобразуем объект datetime в строку формата "ДД.ММ.ГГГГ"
    return date_obj.strftime("%d.%m.%Y")

# Примеры использования функции
print(get_date("2024-03-11T02:26:18.671407"))  # Выведет: 11.03.2024
print(get_date("2024-07-13T14:11:29.000000"))  # Выведет: 13.07.2024
