import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def phone1():
    return Phone("Смартфон", 10000, 20, 1)
def test_phone_init(phone1):
    assert phone1.name == "Смартфон"
    assert phone1.price == 10000
    assert phone1.quantity == 20
    assert phone1.number_of_sim == 1

def test_phone_repr(phone1):
    assert repr(phone1) == "Phone('Смартфон', 10000, 20, 1)"

def test_number_of_sim(phone1):
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == 2



