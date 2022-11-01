from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path("admin/", admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularRedocView.as_view(url_name='schema')),
    path("api/users/", include("users.urls")),
    path("api/login/", ObtainAuthToken.as_view(), name="login"),
]
