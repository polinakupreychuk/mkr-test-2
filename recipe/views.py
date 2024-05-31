from django.shortcuts import render, get_object_or_404
from .models import Recipe
from datetime import datetime

def main(request):
    # Filter recipes created in the year 2023
    recipes = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    # Get the specific recipe by ID
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
