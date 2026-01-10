from src.product import Product


class Category:
    """Класс для создания категорий"""
    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        # Приватный атрибут: доступ только внутри класса
        self.__products = []  # Инициализируем пустой список
        # Добавляем начальные товары, если они переданы
        if products:
            for product in products:
                self.add_product(product)

    @property
    def products(self):
        """Геттер для доступа к списку товаров (только чтение)"""
        return self.__products

    @property
    def product_count(self):
        """Возвращает количество товаров в категории."""
        return len(self.__products)

    def add_product(self, product):
        """Метод для добавления товара в категорию.
        Проверяет, что переданный объект — экземпляр Product"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product.")
        self.__products.append(product)
