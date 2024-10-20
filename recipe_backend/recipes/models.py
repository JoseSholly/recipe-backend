from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        # Fetch all related recipe names and join them with commas
        recipes = self.recipe_set.all()  # Access related Recipe objects
        recipe_names = ', '.join([recipe.food_name for recipe in recipes])
        
        return f"{self.name} ({recipe_names})" if recipe_names else self.name

class Recipe(models.Model):
    food_name = models.CharField(max_length=255)
    preparation_time = models.CharField(max_length=100)
    cooking_time = models.CharField(max_length=100)
    total_time = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    servings = models.IntegerField()
    calories = models.IntegerField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    preparation_instructions = models.TextField()

    def __str__(self):
        return self.food_name