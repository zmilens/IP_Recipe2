from django import urls
from django.conf.urls import url, include
from rest_framework.exceptions import server_error
from .views import AuthorsViewset, CustomAuthToken, RecipeViewset, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf.urls.static import static
from django.conf import settings

from api import views

router = DefaultRouter()
router.register('recipe', RecipeViewset, basename='recipe')
router.register('author', AuthorsViewset, basename='author')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    url(r'api_author/$', views.AuthorsApi),
    url(r'api_category/$', views.CategoryApi),
    url(r'api_kitchen/$', views.KitchenApi),
    url(r'api_author/([0-9]+)$', views.AuthorsApi),
    url(r'api_recipe/$', views.RecipeApi),
    url(r'api_recipe/([0-9]+)$', views.RecipeApi),
    url('', include(router.urls)),
    url(r'^auth/', CustomAuthToken.as_view(),),
    url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)