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
        """
        Создает объект Product из словаря с атрибутами.
        Пример: {'name': 'Apple', 'price': 10, 'quantity': 5}
        """
        name = product_info.get("name")
        price = product_info.get("price", 0)
        quantity = product_info.get("quantity", 0)
        if name is None:
            raise ValueError("В словаре должен быть ключ 'name'.")
        return cls(name, price, quantity)


class Category:
    """Класс для создания категорий"""

    category_count = 0  # Количество созданных категорий
    total_products = 0  # Общее число товаров во всех категориях

    def __init__(self, name):
        self._name = name
        self.__products = {}  # Приватный словарь товаров
        Category.category_count += 1

    @property
    def name(self):
        return self._name

    @property
    def products(self):
        """Возвращает строку со всеми продуктами в формате"""
        if not self.__products:
            return "Нет товаров в категории."
        product_list = []
        for product in self.__products.values():
            product_list.append(f"{product.name}: {product.quantity} шт. по цене {product.price}")
        return "\n".join(product_list)

    def add_product(self, product, quantity=1):
        if not isinstance(product, Product):
            print("Это не объект Product")
            return
        if product.name in self.__products:
            existing_product = self.__products[product.name]
            existing_product.quantity += quantity
            existing_product.price = product.price
            print(f"Обновлено количество и цена товара '{product.name}': {existing_product.quantity} шт.")
        else:
            product_copy = Product(product.name, product.price, quantity)  # Создаем копию товара
            self.__products[product_copy.name] = product_copy
            # Обновляем общее число товаров
            Category.total_products += quantity
            print(f"Добавлен товар '{product_copy.name}', количество: {quantity} шт.")
