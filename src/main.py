# Определение класса Product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Определение класса Category
class Category:
    def __init__(self, name):
        self.name = name
        self.products = {}  # словарь для хранения продуктов и их количества

    def add_product(self, product, quantity):
        if product.name in self.products:
            self.products[product.name]['quantity'] += quantity
        else:
            self.products[product.name] = {'product': product, 'quantity': quantity}

    def show_products(self):
        print(f"Категория: {self.name}")
        for p_info in self.products.values():
            product = p_info['product']
            quantity = p_info['quantity']
            print(f"{product.name}: {quantity} шт. по цене {product.price}")

# Основной код, где создаются продукты и категории
def main():
    # Создаем категории
    electronics = Category("Электроника")
    books = Category("Книги")

    # Создаем продукты
    smartphone = Product("Смартфон", 29999)
    laptop = Product("Ноутбук", 59999)
    roman = Product("Роман", 500)

    # Добавляем продукты в категории
    electronics.add_product(smartphone, 3)  # добавляем 3 смартфона
    electronics.add_product(laptop, 2)      # добавляем 2 ноутбука
    books.add_product(roman, 15)              # добавляем 15 романов

    # Выводим состав категории
    electronics.show_products()
    books.show_products()

if __name__ == "__main__":
    main()
