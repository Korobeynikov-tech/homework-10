from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


def test_filter_by_currency():
    transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },{
              "id": 143264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "RUB",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]

    currency = 'USD'

    # filtered_transactions = list(filter_by_currency(transactions, currency))
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == transactions[0]
    assert next(generator) == transactions[1]


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
    assert next(generator) == "0000 0000 0000 1000"
    assert next(generator) == "0000 0000 0000 1001"
    assert next(generator) == "0000 0000 0000 1002"
