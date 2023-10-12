"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone



@pytest.fixture
def item1():
    """Создаем экземпляр1 класса в фикстуре"""
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    """Создаем экземпляр2 класса в фикстуре"""
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def phone1():
    """Создаем экземпляр класса в фикстуре"""
    return Phone("iPhone 14", 120_000, 5, 2)


def test_apply_discount(item1, item2):
    Item.pay_rate = 1.0
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 10000.0
    assert item2.price == 20000.0


def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_name(item1):
    assert item1.name == 'Смартфон'


def test_string_to_number(item1):
    assert item1.string_to_number('5') == 5
    assert item1.string_to_number('5.0') == 5
    assert item1.string_to_number('5.5') == 5


def test_repr(item1):
    assert repr(item1) == 'Item("Смартфон", 10000, 20)'


def test_str(item1):
    assert str(item1) == "Смартфон"


def test_add(item1, phone1):
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
