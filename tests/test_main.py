import pytest

from src.main import Category, Product


@pytest.fixture
def sample_product():
    return Product("Мяч", "Поверхностный мяч для игры", 15.99, 10)


@pytest.fixture
def sample_category():
    return Category("Игрушки", "Детские игрушки")


def test_product_initialization():
    product = Product("Карандаш", "Графитный карандаш", 0.99, 100)
    assert product.name == "Карандаш"
    assert product.description == "Графитный карандаш"
    assert product.price == 0.99
    assert product.quantity == 100


def test_category_initialization_without_products():
    initial_category_count = Category.category_count
    initial_total_products = Category.total_products

    cat = Category("Дом", "Товары для дома")
    assert cat.name == "Дом"
    assert cat.description == "Товары для дома"
    assert isinstance(cat.products, list)
    assert len(cat.products) == 0
    # Проверка счетчиков
    assert Category.category_count == initial_category_count + 1
    assert Category.total_products == initial_total_products


def test_category_initialization_with_products():
    products = [Product("Мяч", "Поверхностный мяч", 10.0, 5), Product("Ракетка", "Ракетка для тенниса", 20.0, 2)]
    initial_category_count = Category.category_count
    initial_total_products = Category.total_products

    cat = Category("Спорт", products=products)
    assert len(cat.products) == 2
    # Проверка счетчиков
    assert Category.category_count == initial_category_count + 1
    assert Category.total_products == initial_total_products + 2


def test_add_product_increases_total_products():
    category = Category("Кухня")
    initial_total_products = Category.total_products
    product = Product("Нож", "Нож для приготовления", 5.99, 20)
    category.add_product(product)
    assert product in category.products
    assert Category.total_products == initial_total_products + 1
