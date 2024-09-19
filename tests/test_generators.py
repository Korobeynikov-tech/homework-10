from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


def test_filter_by_currency():
    transactions = [{'currency': 'USD', 'amount': 100}, {'currency': 'EUR', 'amount': 50},
                    {'currency': 'USD', 'amount': 75}]
    currency = 'USD'

    # filtered_transactions = list(filter_by_currency(transactions, currency))
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[2]


def test_transaction_descriptions():
    transactions = [{'description': 'payment'}, {'description': 'refund'}, {'description': 'purchase'}]

    # descriptions = list(transaction_descriptions(transactions))
    generator = transaction_descriptions(transactions)
    assert next(generator) == transactions[0]['description']
    assert next(generator) == transactions[1]['description']
    assert next(generator) == transactions[2]['description']


def test_card_number_generator():
    start = 1000
    stop = 1005

    # card_numbers = list(card_number_generator(start, stop))
    generator = card_number_generator(start, stop)
    assert next(generator) == 1000
    assert next(generator) == 1001
    assert next(generator) == 1002
