import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
    """Создаем экземпляр класса в фикстуре"""
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str(phone1):
    assert str(phone1) == 'iPhone 14'


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 2