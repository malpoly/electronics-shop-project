import csv

from src.item import Item

class Phone(Item):
    """
       Класс для представления товара в магазине.
       атрибут, содержащий количество поддерживаемых сим-карт
       """
    def __init__(self, name, price, quantity, number_of_sim) -> None:
        """
                Создание экземпляра класса phone.

                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                :param number_of_sim: Количество сим-карт.
                """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, value):
        if value > 0:
            self.__number_of_sim = value
        else:
            print(ValueError('Количество физических SIM-карт должно быть целым числом больше нуля'))



