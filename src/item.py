import csv

class InstantiateCSVError(Exception):
    pass


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
        super().__init__
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'


    def __str__(self):
        return f"{self.name}"


    def __add__(self, other):
        return self.quantity + other.quantity



    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        if len(self.__name) < 10:
            self.__name = name
        else:
            print(self.__name[:10])


    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv'):
        try:
            with open(filename, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    __name = str(row['name'])
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    if row['name'] or row['price'] or row['quantity'] is None:
                        raise InstantiateCSVError
                    item = cls(__name, price, quantity)
                    print(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")





    @staticmethod
    def string_to_number(price):
        return int(float(price))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return float(self.price * Item.pay_rate)