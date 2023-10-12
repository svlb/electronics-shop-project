from src.item import Item


class Mixinlang:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, Mixinlang):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)