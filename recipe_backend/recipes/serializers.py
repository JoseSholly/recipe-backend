from rest_framework import serializers
from .models import Recipe, Ingredient
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "profile_picture"]

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']

class RecipeCreateSerializer(serializers.ModelSerializer):
    # ingredients = serializers.ListField(
    #     child=serializers.DictField(
    #         child=serializers.CharField()
    #     ),
    #     write_only=True
    # )
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'food_name','image','mood','weather','energy','hunger','dietary','allergies', 'budget','preparation_time', 'cooking_time', 
                 'total_time', 'course', 'cuisine', 'servings', 'calories',
                 'ingredients', 'preparation_instructions']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        
        # Create ingredients for the recipe
        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(
                name=ingredient_data.get('name', ''),
                quantity=ingredient_data.get('quantity', '')
            )
            recipe.ingredients.add(ingredient)
        
        return recipe
    
class RecipeListSerializer(serializers.ModelSerializer):
    # ingredients = serializers.ListField(
    #     child=serializers.DictField(
    #         child=serializers.CharField()
    #     ),
    #     write_only=True
    # )
    ingredients = IngredientSerializer(many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            "user",
            "id",
            "food_name",
            "image",
            "mood",
            "weather",
            "energy",
            "hunger",
            "dietary",
            "allergies",
            "budget",
            "preparation_time",
            "cooking_time",
            "total_time",
            "course",
            "cuisine",
            "servings",
            "calories",
            "ingredients",
            "preparation_instructions",
        ]

        

class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'food_name','image','mood','weather','energy','hunger','dietary','allergies', 'budget','preparation_time','cooking_time', 
                 'total_time', 'course', 'cuisine', 'servings', 'calories',
                 'ingredients', 'preparation_instructions' ]