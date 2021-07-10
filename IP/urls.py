from api import urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include



urlpatterns = [
    url(r'^', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('api.urls'))
]

