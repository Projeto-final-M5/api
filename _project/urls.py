from django.contrib import admin
from django.urls import path, include
from users.views import LoginView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularRedocView.as_view(url_name='schema')),
    path("api/users/", include("users.urls")),
    path("api/login/", LoginView.as_view(), name="login"),
]
