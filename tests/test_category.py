import pytest
from src.category import Category
from src.product import Product


class TestCategory:
    def test_add_product_duplicate(self):
        """Тест добавления дубликата продукта (проверка уникальности не реализована — проверяем логику списка)"""
        category = Category("Test Category", "Test description")
        product = Product("Test Product", "Test description", 100.0, 5)
        category.add_product(product)
        category.add_product(product)  # Добавляем дважды
        assert category.product_count == 2  # Проверяем, что дубликаты не фильтруются (если это ожидаемое поведение)

    def test_products_getter_empty(self):
        """Тест геттера products для пустой категории"""
        category = Category("Test Category", "Test description")
        assert category.products == ""  # Ожидаем пустую строку для пустых категорий

    def test_product_count_after_remove(self):
        """Тест подсчёта после удаления продукта (если есть метод удаления)"""
        category = Category("Test Category", "Test description")
        product = Product("Test Product", "Test description", 100.0, 5)
        category.add_product(product)
        # Предполагаем метод remove_product
        # category.remove_product(product)
        # assert category.product_count == 0

    def test_init_with_invalid_products(self):
        """Тест инициализации с некорректными продуктами (проверка защиты от TypeError)"""
        with pytest.raises(TypeError):
            Category("Test Category", "Test description", ["not a product"])


    def test_category_description_update(self):
        """Тест изменения описания категории"""
        category = Category("Test Category", "Old description")
        category.description = "New description"
        assert category.description == "New description"

    def test_category_name_update(self):
        """Тест изменения имени категории"""
        category = Category("Old Name", "Test description")
        category.name = "New Name"
        assert category.name == "New Name"
