import pytest

from src.main import Category, Product


def test_product_creation():
    p = Product("Мяч", 100, 5)
    assert p.name == "Мяч"
    assert p.price == 100
    assert p.quantity == 5


def test_price_setter_update_and_negative(monkeypatch):
    p = Product("Ракетка", 20)

    # Проверка изменения цены на большее значение
    p.price = 25
    assert p.price == 25

    # Замена input() на возвращение 'y'
    def fake_input(prompt):
        return "y"

    monkeypatch.setattr("builtins.input", fake_input)

    # Теперь при вызове p.price = 15, подтвердится уменьшение цены
    p.price = 15
    assert p.price == 15

    # Проверка, что отрицательная цена вызывает ошибку
    with pytest.raises(ValueError):
        p.price = -5

    # Проверка, что нечисловая цена вызывает ошибку
    with pytest.raises(ValueError):
        p.price = "новая"


def test_product_new_product_classmethod():
    info = {"name": "Книга", "price": 50, "quantity": 3}
    p = Product.new_product(info)
    assert p.name == "Книга"
    assert p.price == 50
    assert p.quantity == 3

    # Отсутствие ключа 'name' должно вызвать ошибку
    with pytest.raises(ValueError):
        Product.new_product({"price": 10})


def test_category_add_product_and_products_str():
    cat = Category("Спорт")
    p1 = Product("Мяч", 10)
    p2 = Product("Ракетка", 20)
    cat.add_product(p1)
    cat.add_product(p2, quantity=2)

    # Проверяем, что товары добавлены
    output = cat.products
    assert "Мяч: 1 шт." in output
    assert "Ракетка: 2 шт." in output

    # Попытка добавить тот же продукт должна увеличить количество
    p1_dup = Product("Мяч", 10)
    cat.add_product(p1_dup, quantity=3)
    output = cat.products
    assert "Мяч: 4 шт." in output



def test_category_total_and_count():
    initial_count = Category.category_count
    initial_total = Category.total_products
    cat = Category("Электроника")
    assert Category.category_count == initial_count + 1
    p = Product("Телевизор", 30000)
    cat.add_product(p, quantity=2)
    assert Category.total_products >= initial_total + 2
