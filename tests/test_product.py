from src.product import Product


class TestProduct:
    def test_init_product(self):
        """Тест инициализации продукта"""
        product = Product("Test", "Description", 100.0, 5)
        assert product.name == "Test"
        assert product.description == "Description"
        assert product.price == 100.0
        assert product.quantity == 5

    def test_price_setter_valid(self):
        """Тест валидного изменения цены"""
        product = Product("Test", "Description", 100.0, 5)
        product.price = 200.0
        assert product.price == 200.0

    def test_price_setter_invalid_negative(self):
        """Тест установки отрицательной цены (должна быть отклонена)"""
        product = Product("Test", "Description", 100.0, 5)
        product.price = -10.0
        assert product.price == 100.0  # Цена не должна измениться

    def test_price_setter_invalid_zero(self):
        """Тест установки нулевой цены (должна быть отклонена)"""
        product = Product("Test", "Description", 100.0, 5)
        product.price = 0
        assert product.price == 100.0  # Цена не должна измениться

    def test_new_product_method(self):
        """Тест класс-метода new_product"""
        product_data = {"name": "Test Product", "description": "Test description", "price": 100.0, "quantity": 5}
        product = Product.new_product(product_data)
        assert product.name == "Test Product"
        assert product.description == "Test description"
        assert product.price == 100.0
        assert product.quantity == 5

    def test_new_product_duplicate(self):
        """Тест обработки дубликата при использовании new_product"""
        existing_products = [Product("Test Product", "Test description", 100.0, 5)]
        product_data = {"name": "Test Product", "description": "Updated description", "price": 150.0, "quantity": 3}
        product = Product.new_product(product_data, existing_products)
        assert product.quantity == 8  # 5 + 3
        assert product.price == 150.0  # Максимальная цена

    def test_str_method(self):
        """Тест метода __str__."""
        product = Product("Test", "Description", 100.0, 5)
        expected_str = "Test, 100.0 руб. Остаток: 5 шт."
        assert str(product) == expected_str

    def test_price_decrease_confirmation(self, monkeypatch):
        """Тест подтверждения понижения цены (используем monkeypatch для имитации ввода)."""
        product = Product("Test", "Description", 100.0, 5)

        # Имитируем ввод 'y' (подтверждение)
        monkeypatch.setattr("builtins.input", lambda x: "y")
        product.price = 50.0
        assert product.price == 50.0

        # Имитируем ввод 'n' (отмена)
        monkeypatch.setattr("builtins.input", lambda x: "n")
        product.price = 30.0
        assert product.price == 50.0  # Цена не должна измениться
