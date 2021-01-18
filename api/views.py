from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializer import AuthorSerializer, RecipeSerializer, Сategory_productSerializer, IngredientSerializer
from recipes.models import Сategorie, Author, Recipe, Сategory_product, Ingredient
from django.http import JsonResponse

class AuthorViewset(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        author = Author.objects.all()
        return author

class RecipeViewset(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        recipe = Recipe.objects.all()
        return recipe

class Сategory_productViewset(viewsets.ModelViewSet):
    serializer_class = Сategory_productSerializer

    def get_queryset(self):
        category_product = Сategory_product.objects.all()
        return category_product


class IngredientViewset(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        ingredient = Ingredient.objects.all()
        return ingredient
