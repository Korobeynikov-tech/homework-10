# Проект: Фильтрация и сортировка данных

Цель проекта:
Разработать функции для фильтрации списка словарей по значению ключа state и сортировки списка по значению ключа date.

Инструкции по установке:
1. Склонировать репозиторий с проектом.
2. Импортировать функции filter_by_state и sort_by_date в свой проект.

Инструкции по использованию:
1. Вызвать функцию filter_by_state, передав список словарей и опционально значение для ключа state.
2. Вызвать функцию sort_by_date, передав список словарей и необязательный параметр для задания порядка сортировки.

# Пример использования
'''data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(list_of_dicts, state='EXECUTED'):
    return [d for d in list_of_dicts if d.get('state') == state]

filtered_list = filter_by_state(data)
print(filtered_list)


def sort_by_date(dict_list, reverse=True):
    return sorted(dict_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=reverse)

sorted_data = sort_by_date(data)
print(sorted_data)
'''
