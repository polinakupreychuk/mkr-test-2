from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, Category
from datetime import datetime


class RecipeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a category
        self.category = Category.objects.create(name="Main Dishes")
        # Create some sample recipes for testing
        self.recipe1 = Recipe.objects.create(title="Recipe 1", description="Description 1", instructions="Instructions 1", ingredients="Ingredients 1", category=self.category)
        self.recipe2 = Recipe.objects.create(title="Recipe 2", description="Description 2", instructions="Instructions 2", ingredients="Ingredients 2", category=self.category)

    def test_main_view(self):
        # Test main view
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)  # Check if the status code is 200 (OK)
        self.assertTemplateUsed(response, 'main.html')  # Check if the correct template is being used
        self.assertQuerysetEqual(response.context['recipes'], Recipe.objects.filter(created_at__year=2023))  # Check if the correct recipes are in the context

    def test_recipe_detail_view(self):
        # Test recipe detail view
        response = self.client.get(reverse('recipe_detail', args=(self.recipe1.id,)))
        self.assertEqual(response.status_code, 200)  # Check if the status code is 200 (OK)
        self.assertTemplateUsed(response, 'recipe_detail.html')  # Check if the correct template is being used
        self.assertEqual(response.context['recipe'], self.recipe1)  # Check if the correct recipe is in the context
