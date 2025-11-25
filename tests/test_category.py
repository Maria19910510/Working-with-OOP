from src.category import Category
from src.product import Product


def test_category_add_product_and_products_str():
    cat = Category("Спорт")
    p1 = Product("Мяч", 10)
    p2 = Product("Ракетка", 20)
    # Добавляем продукты
    cat.add_product(p1)
    cat.add_product(p2, quantity=2)

    # Проверяем вывод
    output = cat.products
    assert "Мяч: 1 шт." in output
    assert "Ракетка: 2 шт." in output

    # Добавляем тот же продукт еще раз
    p1_dup = Product("Мяч", 10)
    cat.add_product(p1_dup, quantity=3)
    output = cat.products
    assert "Мяч: 4 шт." in output

def test_category_total_and_count():
    initial_count = Category.category_count
    initial_total = Category.total_products
    cat = Category("Электроника")
    # Проверка увеличения количества категорий
    assert Category.category_count == initial_count + 1
    p = Product("Телевизор", 30000)
    cat.add_product(p, quantity=2)
    # Проверка увеличения общего числа товаров
    assert Category.total_products >= initial_total + 2

def test_add_non_product_object():
    cat = Category("Недействительные товары")
    result = cat.add_product("Не продукт")
    # Поскольку мы используем print, можно проверить вывод или убедиться, что ничего не добавилось
    assert "Нет товаров в категории." == cat.products or cat.products.startswith("Нет товаров")


def test_products_empty():
    cat = Category("Пустая категория")
    assert cat.products == "Нет товаров в категории."

def test_multiple_products():
    cat = Category("Много товаров")
    products = [
        Product("Книга", 500),
        Product("Ручка", 50),
        Product("Тетрадь", 70)
    ]
    for p in products:
        cat.add_product(p)
    output = cat.products
    assert "Книга: 1 шт." in output
    assert "Ручка: 1 шт." in output
    assert "Тетрадь: 1 шт." in output

def test_product_price_update():
    cat = Category("Обновление цены")
    p = Product("Кофе", 300)
    cat.add_product(p)
    # Обновляем цену товара и добавляем еще
    p_new = Product("Кофе", 350)
    cat.add_product(p_new, quantity=2)
    output = cat.products
    # Проверяем, что количество увеличилось
    assert "Кофе: 3 шт." in output


def test_total_products_accumulates_correctly():
    initial_total = Category.total_products
    cat1 = Category("Категория 1")
    cat2 = Category("Категория 2")
    p1 = Product("Товар1", 100)
    p2 = Product("Товар2", 200)
    cat1.add_product(p1, quantity=2)
    cat2.add_product(p2, quantity=3)
    # Общее число должно увеличиться
    expected_total = initial_total + 2 + 3
    assert Category.total_products >= expected_total
