def filter_by_state(list_of_dicts, state='EXECUTED'):

    """Фильтрование списка словарей по указанному состоянию.

        data:
            args: List[Dict[str, Any]] - Список словарей для фильтрации

        state:
            str: Состояние, по которому выполняется фильтрация

        return:
             List[Dict[str, Any]] - Список словарей с указанным состоянием
    """

    return [d for d in list_of_dicts if d.get('state') == state]

# Пример использования
data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

filtered_list = filter_by_state(data)
print(filtered_list)


def sort_by_date(dict_list, reverse=True):

    """Сортировка списка словарей по дате.

        data:
            args: List[Dict[str, Any]] - Список словарей для сортировки

        return:
            args: List[Dict[str, Any]] - Список словарей, отсортированных по дате
    """

    return sorted(dict_list, key=lambda x: x.get("date"), reverse=reverse)

# Пример использования
data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

sorted_data = sort_by_date(data)
print(sorted_data)
