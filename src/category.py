from src.product import Product


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
            # Создаем копию товара через класс Product
            product_copy = Product(product.name, product.price, quantity)
            self.__products[product.name] = product_copy
            print(f"Товар '{product.name}' добавлен в категорию.")
            # Обновляем общее число товаров
            Category.total_products += quantity
            print(f"Добавлен товар '{product_copy.name}', количество: {quantity} шт.")
