from django.urls import path

from rest_framework.authtoken import views

from . import views

urlpatterns = [
    path("", views.UserView.as_view(), name="users"),
]
