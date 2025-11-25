import pytest
from src.product import Product


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

    # Замена input() на возвращение 'y' для подтверждения уменьшения цены
    def fake_input(prompt=""):
        return "y"

    monkeypatch.setattr("builtins.input", fake_input)

    # Уменьшение цены — подтверждение через input
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

    # Отсутствие ключа 'name' вызывает ошибку
    with pytest.raises(ValueError):
        Product.new_product({"price": 10})
