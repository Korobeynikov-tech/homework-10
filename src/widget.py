# Добавляем функции get_mask_card_number и get_mask_account в модуль widget
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

def mask_account_card(info):
    if 'Счет' in info:
        # Маскировка номера счета
        account_number = info.split()[-1]
        masked_number = get_mask_card_number(account_number)
        return info.replace(account_number, masked_number)
    else:
        # Маскировка номера карты
        card_number = info.split()[-1]
        masked_number = get_mask_account(card_number)
        return info.replace(card_number, masked_number)

# Примеры использования функции
print(mask_account_card("Maestro 1596837868705199")) # Maestro ************5199
print(mask_account_card("Счет 64686473678894779589")) # Счет ****************9589
print(mask_account_card("MasterCard 7158300734726758")) # MasterCard ************6758
print(mask_account_card("Счет 35383033474447895560")) # Счет ****************5560
print(mask_account_card("Visa Classic 6831982476737658")) # Visa Classic ************7658
print(mask_account_card("Visa Platinum 8990922113665229")) # Visa Platinum ************5229
print(mask_account_card("Счет 73654108430135874305")) # Счет ****************4305
