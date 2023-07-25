from django.urls import path

from .views import BookFollowView, BookFollowViewCreate

urlpatterns = [
    path("books/follow/", BookFollowView.as_view()),
    path("books/<copy_id>/follow/", BookFollowViewCreate.as_view()),
]
