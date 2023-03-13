import pytest
from src.item import Item

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)
def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

def test_item_calculate_total_price(item1):
    assert 200000

def test_item_apply_discount(item1):
    Item.pay_rate = 0.8
    assert 8000
