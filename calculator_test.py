import pytest
from app.calculator import my_add


def test_myadd():
    number1 = 2,
    number2 = 3,
    assert my_add(number1, number2) == 2, f"Проверка сложения числа {number1} и {number2}"
