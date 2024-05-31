from django.test import TestCase
from django.utils import timezone
from .models import Recipe, Category

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Test Category')

    def setUp(self):
        # Set up modified objects used by test methods
        self.category = Category.objects.get(id=1)
        Recipe.objects.create(title='Test Recipe', description='Test Description', category=self.category)

    def test_recipe_creation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.description, 'Test Description')
        self.assertEqual(recipe.category, self.category)
        self.assertTrue(recipe.created_at <= timezone.now())
        self.assertTrue(recipe.updated_at <= timezone.now())

    def test_recipe_str(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.title)

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

    def test_category_str(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), category.name)
