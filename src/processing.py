from datetime import datetime

def filter_by_state(list_of_dicts, state='EXECUTED'):
    return [d for d in list_of_dicts if d.get('state') == state]
'''
Фильтрование списка словарей 

 data: Список словарей для фильтрации
 state: Состояние, по которому выполняется фильтрация
return: Список словарей с указанным состоянием
'''

# Пример использования
data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

filtered_list = filter_by_state(data)
print(filtered_list)


def sort_by_date(dict_list, reverse=True):
    return sorted(dict_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=reverse)
'''
Сортировка списка словарей по дате.

data: Список словарей 
reverse: Логический флаг для сортировки в обратном порядке, значение по умолчанию равно True
return: Список словарей, отсортированных по True
'''

# Пример использования
data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

sorted_data = sort_by_date(data)
print(sorted_data)
