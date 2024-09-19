def filter_by_currency(transactions, currency):
    """
    Функция фильтрует список транзакций по валюте и возвращает только те транзакции, у которых валюта совпадает с заданной.
    """
    for transaction in transactions:
        if transaction.get('currency') == currency:
            yield transaction

def transaction_descriptions(transactions):
    """
    Функция принимает список транзакций и возвращает описания всех транзакций.
    """
    for transaction in transactions:
        yield transaction.get('description')

def card_number_generator(start, stop):
    """
    Функция-генератор генерирует последовательность номеров карт от start до stop.
    """
    for card_number in range(start, stop):
        yield card_number
