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


print(get_date("2024-03-11T02:26:18.671407"))  # Выведет: 11.03.2024
print(get_date("2024-07-13T14:11:29.000000"))  # Выведет: 13.07.2024
