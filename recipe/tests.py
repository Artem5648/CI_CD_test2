from django.test import TestCase
from .models import Category, Recipe


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")

        self.assertEqual(category.name, "Desserts")

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Course")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Pasta",
            description="Delicious pasta",
            instructions="Boil water, add pasta...",
            ingredients="Pasta, salt, water",
            category=self.category
        )
        self.assertEqual(recipe.title, "Pasta")
        self.assertEqual(recipe.category.name, "Main Course")
