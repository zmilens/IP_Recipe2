from rest_framework import serializers
from recipes.models import Authors, Recipe, Kitchen, Сategorie
from django.contrib.auth.models import User



class RecipeSerializer(serializers.ModelSerializer):
    # kitchen = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()
    # author = serializers.StringRelatedField()
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'kitchen', 'ingredients', 'description', 'published', 'author', 'photo']


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = ['authorId', 'name', 'surname', 'photo']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['is_superuser']

class KitchenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kitchen
        fields = ['id', 'kitchen']

class СategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Сategorie
        fields = ['id', 'category']
   