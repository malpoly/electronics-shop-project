import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)
def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_item_apply_discount(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) != 0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.6') == 5

def test_item__repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_item__str__(item1):
    assert str(item1) == 'Смартфон'

def test__add__():
    class Apple():
        def __init__(self, name, price, quantity):
            self.__name = name
            self.price = price
            self.quantity = quantity

    item2 = Item("Смартфон", 20000, 30)
    item3 = Item("Смартфон", 30000, 40)
    phone1 = Phone("Айфон 10", 60000, 50, 1)
    phone2 = Phone("Айфон 12", 160000, 10, 1)
    iphone1 = Apple("Айфон 13", 180000, 5)
    assert phone1 + phone2 == 60
    assert item2 + item3 == 70
    assert item2 + phone2 == 40
    assert phone1 + item3 == 90
    #assert phone1 + iphone1 == TypeError('Складывать можно только объекты Item и дочерние от них.')
