"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_calculate_total_price():
     assert calculate_total_price(10000, 20) == 20000
     assert calculate_total_price(30000, 5) == 150000


def test_apply_discount():
     assert apply_discount(10000, 1.0) == 10000.0
     assert apply_discount(30000, 1.0) == 30000.0
     assert apply_discount(10000 , 0.8) == 8000.0
