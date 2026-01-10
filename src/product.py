class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = None  # Приватный атрибут
        self.quantity = quantity
        self.price = price  # Используем сеттер для валидации

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута __price."""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер с валидацией и запросом подтверждения при понижении цены."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return  # Не меняем цену

        if self.__price is not None and value < self.__price:
            # Спрашиваем подтверждение при понижении цены
            response = input(f"Цена понижается с {self.__price} до {value}. Подтвердить (y/n)? ").strip().lower()
            if response != "y":
                print("Изменение цены отменено.")
                return

        self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict, product_list: list = None) -> "Product":
        """Класс‑метод для создания продукта из словаря.
        Если товар с таким именем уже есть в product_list, объединяет количество и берёт максимальную цену"""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        # Проверка на дубликат, если передан список товаров

        if product_list is not None:
            for existing_product in product_list:
                if existing_product.name == name:
                    # Объединяем количество
                    existing_product.quantity += quantity
                    # Выбираем максимальную цену
                    existing_product.price = max(existing_product.price, price)
                    return existing_product  # Возвращаем уже существующий объект

        # Если дубликата нет — создаём новый товар
        return cls(name, description, price, quantity)
