import pytest

# 1
def my_subtract(a, b):
    return a - b

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (10, 5, 5),
    (20, 10, 10),
])
def test_my_subtract(a, b, expected):
    assert my_subtract(a, b) == expected

# 2 

class MyGreatException(Exception):
    pass

class NegativeResultError(Exception):
    pass

def my_add(a, b):
    result = a + b
    if result < 0:
        raise NegativeResultError("Result is negative")
    return result

def test_negative_result_error():
    with pytest.raises(NegativeResultError):
        my_add(-2, -3)

# 3 

import tempfile
import os

@pytest.fixture
def temp_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"Hello, world!")
        temp_filename = f.name

    yield temp_filename

    os.remove(temp_filename)

def test_temp_file(temp_file):
    with open(temp_file, "rb") as f:
        content = f.read()

    assert content == b"Hello, world!"

# 4 
@pytest.fixture
def my_multiply():
    def _multiply(a, b):
        return a * b

    return _multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (4, 5, 20),
    (6, 7, 42),
])
def test_my_multiply(my_multiply, a, b, expected):
    assert my_multiply(a, b) == expected


# 5 

from datetime import datetime

def get_todays_date():
    return datetime.now().strftime("%Y-%m-%d")

def test_get_todays_date(monkeypatch):
    class FakeDateTime:
        @staticmethod
        def now():
            return datetime(2023, 4, 21)

    monkeypatch.setattr("datetime.datetime", FakeDateTime)

    assert get_todays_date() == "2023-04-21"
