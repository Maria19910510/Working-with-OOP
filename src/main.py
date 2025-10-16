class Product:
    """Класс для создания продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для создания категорий"""

    category_count = 0  # Атрибут класса: количество созданных категорий
    total_products = 0  # Атрибут класса: общее количество товаров во всех категориях

    def __init__(self, name: str, description: str = "", products=None):
        self.name = name
        self.description = description
        # Если список товаров не передан, создаем пустой список
        if products is None:
            self.products = []
        else:
            self.products = products

        # Повышаем счетчик категорий
        Category.category_count += 1

        # Обновляем общее количество товаров
        Category.total_products += len(self.products)

    def add_product(self, product: Product):
        """Добавляет товар в категорию и обновляет общее число товаров"""
        self.products.append(product)
        Category.total_products += 1
