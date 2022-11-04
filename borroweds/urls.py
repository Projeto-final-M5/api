from django.urls import path

from rest_framework.authtoken import views

from . import views

urlpatterns = [
    path('borrowed/<pk>/book/', views.BorrrowedListCreateView.as_view()),
]
