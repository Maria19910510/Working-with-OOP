class Product:
    """Класс для создания продуктов"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

class Category:
    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for product in products:
                self.add_product(product)

    @property
    def products(self) -> str:
        if not self.__products:
            return ""
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self) -> int:
        return len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product.")
        self.__products.append(product)



if __name__ == "__main__":
    # Создаём товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    product2 = Product("iPhone 15", "512GB, Gray", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаём категорию с товарами
    category1 = Category(
        "Смартфоны",
        "Мобильные устройства для повседневных задач",
        [product1, product2, product3]
    )

    # Выводим список товаров через геттер
    print("Список товаров в категории:")
    print(category1.products)
    # Вывод:
    # Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
    # iPhone 15, 210000.0 руб. Остаток: 8 шт.
    # Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.

    # Добавляем новый товар
    product4 = Product("55\" QLED 4K", "Телевизор с подсветкой", 123000.0, 7)
    category1.add_product(product4)

    print(f"\nВсего товаров: {category1.product_count}")
    print("Обновлённый список:")
    print(category1.products)
