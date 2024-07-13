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
