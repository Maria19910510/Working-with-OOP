from unittest.mock import patch

import pytest

from src.main import Category, Product


@pytest.fixture
def sample_product():
    return Product("Мяч", 15.99, 10)

@pytest.fixture
def sample_category():
    return Category("Игрушки")

def test_product_initialization():
    product = Product("Карандаш", 0.99, 100)
    assert product.name == "Карандаш"
    assert product.price == 0.99
    assert product.quantity == 100

def test_category_initialization_without_products():
    initial_category_count = Category.category_count
    initial_total_products = Category.total_products

    cat = Category("Дом")
    assert cat.name == "Дом"
    assert isinstance(cat.products, list)
    assert len(cat.products) == 0
    # Проверка счетчиков
    assert Category.category_count == initial_category_count + 1
    assert Category.total_products == initial_total_products

def test_category_initialization_with_products():
    products = [
        Product("Мяч", 10.0, 5),
        Product("Ракетка", 20.0, 2)
    ]
    initial_category_count = Category.category_count
    initial_total_products = Category.total_products

    cat = Category("Спорт")
    # Добавляем продукты вручную, т.к. в конструкторе их не передают
    for p in products:
        cat.add_product(p)

    assert len(cat.products) == 2
    # Проверка счетчиков - потребуется дождаться корректных увеличений
    assert Category.category_count == initial_category_count + 1
    # Общие товары увеличились
    assert Category.total_products >= initial_total_products + 2

def test_add_product_increases_total_products():
    category = Category("Кухня")
    initial_total_products = Category.total_products
    product = Product("Нож", "Нож для приготовления", 5.99)
    category.add_product(product)
    assert any(p[0] == "Нож" for p in category.products)
    assert Category.total_products >= initial_total_products + 1

def test_price_setter_confirmation(monkeypatch):
    product = Product("Лампа", 50, 5)
    # Симулируем подтверждение "нет" (отказ)
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    original_price = product.price
    product.price = 40  # Попытка снизить цену
    assert product.price == original_price  # Цена не должна измениться

    # Симулируем подтверждение "да"
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product.price = 40  # Теперь цена должна измениться
    assert product.price == 40

def test_add_product_update_quantity_and_price():
    category = Category("Техника")
    product1 = Product("Телевизор", 30000, 2)
    category.add_product(product1)

    # Создаём продукт с тем же названием, другой ценой
    product2 = Product("Телевизор", 32000, 3)
    with patch('builtins.input', return_value='y'):  # Подтверждение изменения цены
        category.add_product(product2)

    # Проверяем, что количество увеличилось, цена обновилась
    product_in_cat = category._products["Телевизор"]
    assert product_in_cat.quantity == 5
    assert product_in_cat.price == 32000