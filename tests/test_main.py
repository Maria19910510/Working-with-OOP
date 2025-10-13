import pytest

from src.main import Category, Product


# Фикстура для сброса счетчиков между тестами
@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.total_products = 0
    yield


def test_product_initialization():
    p = Product("Mouse", "Wireless mouse", 25.5, 10)
    assert p.name == "Mouse"
    assert p.description == "Wireless mouse"
    assert p.price == 25.5
    assert p.quantity == 10


def test_category_initialization():
    c = Category("Electronics", "Electronic devices")
    assert c.name == "Electronics"
    assert c.description == "Electronic devices"
    assert isinstance(c.products, list)
    assert len(c.products) == 0


def test_category_count_increment():
    c1 = Category("Books", "Various books")
    c2 = Category("Clothes", "Men's and women's apparel")
    assert Category.category_count == 2


def test_add_product_increases_total_products():
    c = Category("Gadgets", "Various gadgets")
    p1 = Product("Smartphone", "Latest model", 699.99, 5)
    p2 = Product("Tablet", "10 inch display", 299.99, 3)
    c.add_product(p1)
    c.add_product(p2)
    assert len(c.products) == 2
    assert Category.total_products == 2


def test_multiple_categories_and_products():
    c1 = Category("Furniture", "Home furniture")
    c2 = Category("Decor", "Home decor accessories")
    p1 = Product("Sofa", "Comfortable sofa", 500.0, 2)
    p2 = Product("Vase", "Ceramic vase", 25.0, 4)
    c1.add_product(p1)
    c2.add_product(p2)
    assert Category.category_count == 2
    assert Category.total_products == 2
    assert len(c1.products) == 1
    assert len(c2.products) == 1
