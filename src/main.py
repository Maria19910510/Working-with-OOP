class Product:
    """Класс для создания продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для создания категорий"""

    category_count = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        # Увеличиваем количество категорий при создании новой
        Category.category_count += 1

    def add_product(self, product: Product):
        self.products.append(product)
        # Увеличиваем количество всех товаров при добавлении
        Category.total_products += 1
