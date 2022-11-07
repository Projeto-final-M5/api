from django.urls import path

from . import views

urlpatterns = [
    path(
        "feedback/<borrowed_id>/borrowed/",
        views.PostFeedBack.as_view(),
    ),
    path(
        "feedback/",
        views.GetFeedBack.as_view(),
    ),
    path(
        "feedback/<user_id>/user",
        views.GetUserFeedBack.as_view(),
    ),
    path(
        "feedback/<book_id>/book",
        views.GetBookFeedBack.as_view(),
    ),
    path(
        "feedback/<pk>/",
        views.GetFeedBackDatail.as_view(),
    ),
]
