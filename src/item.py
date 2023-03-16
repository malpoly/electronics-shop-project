import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 10:
            self.__name = value
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.pay_rate * self.price)

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        Item.all = [] #Список обнулила, чтобы при проверке работало условие по длине списка = 5, иначе оставался item = Item('Телефон', 10000, 5) в списке
        with open('C:\skypro\lesson_code\lesson_13.1\src\items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])


    @staticmethod
    def string_to_number(number) -> int:
        """статический метод, возвращающий число из числа-строки"""
        return int(float(number))

