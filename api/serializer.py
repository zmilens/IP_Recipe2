from rest_framework import serializers
from recipes.models import Author, Recipe, Сategory_product, Ingredient

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'description', 'published', 'author']


class Сategory_productSerializer(serializers.ModelSerializer):

    class Meta:
        model = Сategory_product
        fields = ['id', 'category_product']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'ingredient']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'author']

