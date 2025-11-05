class Product:
    """Класс для создания продуктов"""

    def __init__(self, name, price, quantity=0):
        self.name = name
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < self._price:
            confirm = input(f"Новая цена {new_price} меньше текущей {self._price}. Продолжить? (y/n): ")
            if confirm.lower() != 'y':
                print("Цена не изменена.")
                return
        if isinstance(new_price, (int, float)) and new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Цена должна быть неотрицательным числом.")


class Category:
    """Класс для создания категорий"""

    category_count = 0  # Атрибут класса: количество созданных категорий
    total_products = 0  # Атрибут класса: общее количество товаров во всех категориях

    def __init__(self, name):
        self._name = name
        self._products = {}  # ключ: название товара, значение: объект Product с количеством

    @property
    def name(self):
        return self._name

    @property
    def products(self):
        # Возвращаем список товаров с их количеством
        return [(product.name, product.price, product.quantity) for product in self._products.values()]

    def add_product(self, product, quantity=1):
        if not isinstance(product, Product):
            print("Это не объект Product")
            return
        if product.name in self._products:
            # Товар уже есть, увеличиваем количество и обновляем цену при необходимости
            existing_product = self._products[product.name]
            existing_product.quantity += quantity
            existing_product.price = product.price  # При необходимости можно обновлять цену
            print(f"Обновлено количество и цена товара '{product.name}': {existing_product.quantity} шт.")
        else:
            # Добавляем новый товар
            product.quantity = quantity
            self._products[product.name] = product
