class Product:
    """Класс для создания продуктов"""

    def __init__(self, name, price, quantity=0):
        self._name = name
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise ValueError("Цена должна быть числом.")
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        if new_price < self.__price:
            confirm = input(f"Новая цена {new_price} меньше текущей {self.__price}. Продолжить? (y/n): ")
            if confirm.lower() != "y":
                print("Цена не изменена.")
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_info):
        """Создает объект Product из словаря с атрибутами.
        Пример: {'name': 'Apple', 'price': 10, 'quantity': 5}"""
        name = product_info.get("name")
        price = product_info.get("price", 0)
        quantity = product_info.get("quantity", 0)
        if name is None:
            raise ValueError("В словаре должен быть ключ 'name'.")
        return cls(name, price, quantity)
