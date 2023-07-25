from django.urls import path

from .views import CopyDetailView, CopyView

urlpatterns = [
    path("books/<pk>/copy", CopyView.as_view()),
    path("copy/<pk>", CopyDetailView.as_view()),
]
