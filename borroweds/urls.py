from django.urls import path

from rest_framework.authtoken import views

from . import views

urlpatterns = [
    path("borrowed/<pk>/book/", views.BorrrowedCreateView.as_view(), name="borrowed"),
]
