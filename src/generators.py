def filter_by_currency(transactions, currency):
    """
    Функция фильтрует список транзакций по валюте и возвращает только те транзакции, у которых валюта совпадает с заданной.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['name'] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Функция принимает список транзакций и возвращает описания всех транзакций.
    """
    for transaction in transactions:
        yield transaction.get('description')


def card_number_generator(start: int, stop: int):
    """
    Функция-генератор генерирует последовательность номеров карт от start до stop.
    """
    for i in range(start, stop):
        result = str(i).zfill(16)
        yield ' '.join([result[0:4], result[4:8], result[8:12], result[12:16]])
