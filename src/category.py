from product import Product


class Category:
    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = []  # Приватный список товаров

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        """Метод для добавления товара в приватный список"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)

    @property
    def products(self) -> str:
        """Геттер, возвращающий список товаров в виде строк"""
        if not self.__products:
            return ""
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self) -> int:
        """Возвращает количество товаров в категории"""
        return len(self.__products)
