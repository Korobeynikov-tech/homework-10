import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.masks import get_date
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
from src.decorators import log
from datetime import datetime


def test_get_mask_card_number_invalid_input():
    with pytest.raises(IndexError):
        get_mask_card_number("1234567890")
    with pytest.raises(IndexError):
        get_mask_card_number("12345678901234567890")
    with pytest.raises(IndexError):
        get_mask_card_number("")
    with pytest.raises(IndexError):
        get_mask_card_number("123456789012345678901234567890")
    with pytest.raises(IndexError):
        get_mask_card_number("12345678901234567890123456789012345678901234567890")
    with pytest.raises(IndexError):
        get_mask_card_number("1")


def test_get_mask_card_number_2_edge_cases():
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"
    assert get_mask_card_number("1234-5678-9012-3456") == "1234 56** **** 3456"
    assert get_mask_card_number("12-3456-7890-1234") == "12 34** **** 1234"


def test_get_mask_card_number_3_invalid_input():
    assert get_mask_card_number(None) == ""
    assert get_mask_card_number("invalid") == "in va lid"
    assert get_mask_card_number("1234abcd5678") == "1234 ab** **** 5678"


# следующая функция
@pytest.mark.parametrize("input_data, expected_output", [
("1234567890123456", "**3456"),
("4111111111111111", "**1111"),
("5105105105105100", "**5100"),
("1234567890", "**7890"),
("9876543210", "**3210")])


def test_get_mask_account(input_data, expected_output):
    assert get_mask_account(input_data) == expected_output


def test_get_mask_account_invalid_input():
    with pytest.raises(IndexError):
        get_mask_account("123")
    with pytest.raises(TypeError):
        get_mask_account(123456789)
    with pytest.raises(ValueError):
        get_mask_account("abcdef")
    with pytest.raises(ValueError):
        get_mask_account("1234567890.12")
    with pytest.raises(ValueError):
        get_mask_account("1234-5678-90")


# следующая функция
def test_standard_date_format():
    assert get_date("2023-05-15T12:30:45.123456") == "15.05.2023"


def test_boundary_date_format():
    assert get_date("2000-01-01T00:00:00.000000") == "01.01.2000"
    assert get_date("9999-12-31T23:59:59.999999") == "31.12.9999"


def test_nonstandard_date_format():
    assert get_date("1999-12-31T00:00:00.123456") == "31.12.1999"
    assert get_date("2023-05-15T12:30:45") == "15.05.2023"


def test_missing_date():
    with pytest.raises(ValueError):
        get_date("2023-05-15T12:30:45")


# следующая функция
def test_filter_by_state_no_state():
    data = [{'state': 'IN_PROGRESS'}, {'state': 'FAILED'}, {'state': 'PENDING'}]
    state = 'EXECUTED'
    assert filter_by_state(data, state) == []


@pytest.mark.parametrize("state, expected",
[('IN_PROGRESS', [{'state': 'IN_PROGRESS'}]),
('FAILED', [{'state': 'FAILED'}]),
('PENDING', [{'state': 'PENDING'}])])


def test_filter_by_state(state, expected):
    data = [{'state': 'IN_PROGRESS'}, {'state': 'FAILED'}, {'state': 'PENDING'}]
    assert filter_by_state(data, state) == expected


# следующая функция
def test_sort_by_date_descending():
    data = [
        {"event": "a", "date": "2023-10-01"},
        {"event": "b", "date": "2021-05-15"},
        {"event": "c", "date": "2022-12-12"},]
    sorted_data = sort_by_date(data)
    assert sorted_data[0]["event"] == "a"  # Самая поздняя дата
    assert sorted_data[1]["event"] == "c"
    assert sorted_data[2]["event"] == "b"


def test_sort_by_date_ascending():
    data = [
        {"event": "a", "date": "2023-10-01"},
        {"event": "b", "date": "2021-05-15"},
        {"event": "c", "date": "2022-12-12"},]
    sorted_data = sort_by_date(data, reverse=False)
    assert sorted_data[0]["event"] == "b"  # Самая ранняя дата
    assert sorted_data[1]["event"] == "c"
    assert sorted_data[2]["event"] == "a"


def test_sort_by_date_identical_dates():
    data = [
        {"event": "a", "date": "2023-10-01"},
        {"event": "b", "date": "2023-10-01"},
        {"event": "c", "date": "2023-10-01"},]
    sorted_data = sort_by_date(data)
    assert sorted_data[0]["event"] == "a"  # Порядок не определен, но все равно должны быть в том же порядке
    assert sorted_data[1]["event"] == "b"
    assert sorted_data[2]["event"] == "c"


def test_sort_by_date_invalid_dates():
    data = [
        {"event": "a", "date": "invalid-date"},
        {"event": "b", "date": "2021-05-15"},
        {"event": "c", "date": None},]
    sorted_data = sort_by_date(data)
    assert sorted_data[0]["event"] == "b"  # 'b' с правильной датой должен быть первым
    assert sorted_data[1]["event"] == "c"  # 'c' с None датой
    assert sorted_data[2]["event"] == "a"  # 'a' с неправильной датой


def test_sort_by_date_non_date_format():
    data = [
        {"event": "a", "date": "1234567890"},
        {"event": "b", "date": "not-a-date"},
        {"event": "c", "date": datetime(2023, 10, 1)},]
    sorted_data = sort_by_date(data, reverse=False)
    assert sorted_data[0]["event"] == "c"
    assert sorted_data[1]["event"] == "a"
    assert sorted_data[2]["event"] == "b"


@pytest.fixture
def card_numbers():
    return ["1234567890123456", "6543210987654321", "8765432198765432", "1234", ""]


@pytest.fixture
def accounts():
    return [
("1234567890123456", "**3456"),
("4111111111111111", "**1111"),
("5105105105105100", "**5100"),
("1234567890", "**7890"),
("9876543210", "**3210")]


@pytest.fixture
def dates():
    return [
("2023-05-15T12:30:45.123456", "15.05.2023"),
("2000-01-01T00:00:00.000000", "01.01.2000"),
("9999-12-31T23:59:59.999999", "31.12.9999"),
("1999-12-31T00:00:00.123456", "31.12.1999"),
("2023-05-15T12:30:45", "15.05.2023")]


@pytest.fixture
def event_data():
    return [
{"event": "a", "date": "2023-10-01"},
{"event": "b", "date": "2021-05-15"},
{"event": "c", "date": "2022-12-12"}]


def test_get_mask_account_1(accounts):
    for acc_number, masked_number in accounts:
        assert get_mask_account(acc_number) == masked_number


def test_get_date(dates):
    for date_str, expected_date in dates:
        assert get_date(date_str) == expected_date


def test_sort_by_date(event_data):
    sorted_data = sort_by_date(event_data)
    assert sorted_data[0]["event"] == "a"
    assert sorted_data[1]["event"] == "c"
    assert sorted_data[2]["event"] == "b"


def test_filter_by_currency(self):
    transactions = [{'currency': 'USD', 'amount': 100}, {'currency': 'EUR', 'amount': 50},
                    {'currency': 'USD', 'amount': 75}]
    currency = 'USD'

    filtered_transactions = list(filter_by_currency(transactions, currency))


def test_transaction_descriptions(self):
    transactions = [{'description': 'payment'}, {'description': 'refund'}, {'description': 'purchase'}]

    descriptions = list(transaction_descriptions(transactions))


def test_card_number_generator(self):
    start = 1000
    stop = 1005

    card_numbers = list(card_number_generator(start, stop))


@log()
def test_func(a, b):
    return a + b


test_func(1, 2)
test_func(3, "a")


@log("logfile.txt")
def test_func2(a, b):
    return a / b


test_func2(4, 2)
test_func2(5, 0)
