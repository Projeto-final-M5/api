from django.urls import path

from rest_framework.authtoken import views

from . import views

urlpatterns = [
    path('book/', views.BookView.as_view()),
    #path('<pk>/', views.UserUpdateView.as_view()),
    #path('<pk>/soft', views.UserDeleteView.as_view()),
]
