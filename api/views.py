from rest_framework import authentication
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import AuthorsSerializer, KitchenSerializer, RecipeSerializer, UserSerializer, СategorySerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from recipes.models import Authors, Kitchen, Recipe, Сategorie
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage

@csrf_exempt
def AuthorsApi(request, id=0):
    if request.method=='GET':
        authors = Authors.objects.all()
        authors_serializer = AuthorsSerializer(authors, many=True)
        return JsonResponse(authors_serializer.data, safe=False)
    elif request.method=='POST':
        authors_data=JSONParser().parse(request)
        authors_serializer = AuthorsSerializer(data=authors_data)
        if authors_serializer.is_valid():
            authors_serializer.save()
            return JsonResponse("Автор добавлен успешно!", safe=False)
        return JsonResponse("Автор не добавлен.", safe=False)
    elif request.method=='PUT':
        authors_data = JSONParser().parse(request)
        authors = Authors.objects.get(authorId=authors_data['authorId'])
        authors_serializer = AuthorsSerializer(authors, data=authors_data)
        if authors_serializer.is_valid():
            authors_serializer.save()
            return JsonResponse("Информация об авторе обновлена успешно!", safe=False)
        return JsonResponse("Информация об авторе не обновлена.", safe=False)
    elif request.method=='DELETE':
        authors = Authors.objects.get(authorId=id)
        authors.delete()
        return JsonResponse("Автор удален из базы данных.", safe=False)

@csrf_exempt
def RecipeApi(request, id=0):
    if request.method=='GET':
        recipes = Recipe.objects.all()
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipes_serializer.data, safe=False)
    elif request.method=='POST':
        recipes_data=JSONParser().parse(request)
        recipes_serializer = RecipeSerializer(data=recipes_data)
        if recipes_serializer.is_valid():
            recipes_serializer.save()
            return JsonResponse("Рецепт добавлен!", safe=False)
        return JsonResponse("Рецепт не добавлен.", safe=False)
    elif request.method=='PUT':
        recipes_data = JSONParser().parse(request)
        recipes = Recipe.objects.get(id=recipes_data['id'])
        recipes_serializer = RecipeSerializer(recipes, data=recipes_data)
        if recipes_serializer.is_valid():
            recipes_serializer.save()
            return JsonResponse("Рецепт обновлен успешно!", safe=False)
        return JsonResponse("Рецепт не обновлен.", safe=False)
    elif request.method=='DELETE':
        recipes = Recipe.objects.get(id=id)
        recipes.delete()
        return JsonResponse("Рецепт удален из базы данных.", safe=False)


@csrf_exempt
def CategoryApi(request, id=0):
    if request.method=='GET':
        category = Сategorie.objects.all()
        category_serializer = СategorySerializer(category, many=True)
        return JsonResponse(category_serializer.data, safe=False)
    elif request.method=='PUT':
        category_data = JSONParser().parse(request)
        category = Сategorie.objects.get(id=category_data['id'])
        category_serializer = СategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(safe=False)
        return JsonResponse(safe=False)
    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        category_serializer = СategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(safe=False)
        return JsonResponse(safe=False)

@csrf_exempt
def KitchenApi(request, id=0):
    if request.method=='GET':
        kitchen = Kitchen.objects.all()
        kitchen_serializer = KitchenSerializer(kitchen, many=True)
        return JsonResponse(kitchen_serializer.data, safe=False)
    elif request.method=='PUT':
        kitchen_data = JSONParser().parse(request)
        kitchen = Kitchen.objects.get(id=kitchen_data['id'])
        kitchen_serializer = KitchenSerializer(kitchen, data=kitchen_data)
        if kitchen_serializer.is_valid():
            kitchen_serializer.save()
            return JsonResponse(safe=False)
        return JsonResponse(safe=False)
    elif request.method=='POST':
        kitchen_data=JSONParser().parse(request)
        kitchen_serializer = KitchenSerializer(data=kitchen_data)
        if kitchen_serializer.is_valid():
            kitchen_serializer.save()
            return JsonResponse(safe=False)
        return JsonResponse(safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)



class AuthorsViewset(viewsets.ModelViewSet):
    serializer_class = AuthorsSerializer

    def get_queryset(self):
        author = Authors.objects.all()
        return author

class RecipeViewset(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        recipe = Recipe.objects.all()
        return recipe


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'is_superuser': user.is_superuser,
        })

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

