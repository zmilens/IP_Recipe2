from django.conf.urls import url, include
from .views import  AuthorViewset, RecipeViewset, Сategory_productViewset, IngredientViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('recipe', RecipeViewset, basename='recipe')
router.register('category_product', Сategory_productViewset, basename='category_product')
router.register('ingredient', IngredientViewset, basename='ingredient')
router.register('author', AuthorViewset, basename='author')

urlpatterns = [
    url('', include(router.urls)),


]