from django.urls import path

from . import views

urlpatterns = [
    path(
        "feedback/<int:borrowed_id>/borrowed/",
        views.PostFeedBack.as_view(),
    ),
    path(
        "feedback/",
        views.GetFeedBack.as_view(),
    ),
    path(
        "feedback/<int:user_id>/user/",
        views.GetUserFeedBack.as_view(),
    ),
    path(
        "feedback/<int:book_id>/book/",
        views.GetBookFeedBack.as_view(),
    ),
    path(
        "feedback/<pk>/",
        views.GetFeedBackDatail.as_view(),
    ),
]
