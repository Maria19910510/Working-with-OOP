import json
from src.main import Category, Product


def load_categories_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for cat_data in data["categories"]:
        category = Category(cat_data["name"], cat_data["description"])
        for prod_data in cat_data["products"]:
            product = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                quantity=prod_data["quantity"],
            )
            category.add_product(product)
        categories.append(category)
    return categories
